import botocore

import requests
import getpass
import json
import sys
import os
import re
import pandas as pd
from IPython.display import HTML
from IPython.display import display

from datetime import datetime, timezone, timedelta
from .enums import CheckStatusCode, HTTPStatusCode
from .cassandra_utils import PagedResultHandler
from sqlalchemy import text
from typing import Dict

class SDTcloud():
    def __init__(self):
        self.url = f"http://datalake-internal-query-service.sdt-cloud.svc.cluster.local:8080"  # datalake url
        self.giteamanager_url = f'http://gitea-manager.sdt-cloud.svc.cluster.local:8010'  # gitea-manager url
        self.giteamanager_url_regex = r"((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?"  # gitea url regex
        self.minio_url = f'http://stackbase-minio-service.sdt-cloud.svc.cluster.local:9000'  # minio url
        self.namespace = os.getenv("NAMESPACE")
        self.organizationId = ""
        self.id = ""
        self.email = ""
        self.name = ""
        self.minioBucket = ""
        self.minioAccessKey = ""
        self.minioSecretKey = ""

        # InfluxDB
        self.influxdb_client = None
        self.influxUrl = ""
        self.influxOrganization = ""
        self.influxToken = ""
        self.influxBucket = ""
        self.influxMeasurement = ""

        self.projectDataFrame = None  # project DataFrame
        self.assetDataFrame = None  # asset DataFrame

        self.currentProjectIdx = None  # current project idx
        self.currentProjectName = None  # current project name
        self.currentDevice = None  # current device

        self.minio_client = None

        # TimescaleDB
        self.timescaleDBUrl = 'postgresql://sdt:251327@timescale-db.database.svc.cluster.local:5432/postgres'
        self.timescaledb_conn = None

        # mongodb(TODO: 장비 조회 시, 조회결과로 받아야 할 것)
        self.mongodbUrl = 'mongodb://sdt:251327@mongo-db.database.svc.cluster.local:27017/?authSource=admin'
        self.mongodb_client = None
        # cassandra DB(TODO: 장비 조회 시, 조회결과로 받아야 할 것)
        self.cassandraDBUrl = 'cassandra.database.svc.cluster.local'
        self.cassandraDBPort = 9042
        self.cassandraUser = 'sdt'
        self.cassandraDBPassword = '251327'
        self.cassandra_cluster = None
        self.cassandra_keyspace = None
        self.datetime_pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
        self.gitea_password = 'Sdt251327!'  # gitea password(공통)

    ###################################################### InfluxDB ######################################################

    def initInfluxDB(self, url):
        try:
            import influxdb_client
            self.influxdb_client = influxdb_client.InfluxDBClient(
                url=self.influxUrl,
                token=self.influxToken,
                org=self.influxOrganization
            )
            print('InfluxDB init Success!!')
        except Exception as e:
            raise Exception(e)

    def getMeasurementsFromInfluxBucket(self):
        if self.influxdb_client is None:
            raise AttributeError('Please initInfluxDB function run!!')

        try:
            db_result = self.influxdb_client.buckets_api().find_buckets().buckets
            database_list = [bucket.name for bucket in db_result if bucket.name not in ['_monitoring', '_tasks']]

            table_dict = {}
            for database in database_list:
                query = f'import "influxdata/influxdb/schema" schema.measurements(bucket: "{database}")'
                result = self.influxdb_client.query_api().query(query)
                measurement_list = [row.values["_value"] for table in result for row in table]
                table_dict[database] = measurement_list

            new_data = []
            for key, values in table_dict.items():
                for value in values:
                    new_data.append([key, value])

            df = pd.DataFrame(new_data, columns=['bucket', 'measurement'])
            return df
        except Exception as e:
            raise Exception(e)
    
    def showFieldsFromMeasurement(self, bucket, measurement):
        if self.influxdb_client is None:
            raise AttributeError('Please initInfluxDB function run!!')

        try:
            query_api = self.influxdb_client.query_api()
            # query = f'import "influxdata/influxdb/schema" schema.fields(bucket: "{bucket}", measurement: "{measurement}")'
            query = f'import "influxdata/influxdb/schema"schema.measurementFieldKeys(bucket: "{bucket}",measurement: "{measurement}")'
            result = query_api.query(query)

            field_list = []
            for table in result:
                for record in table.records:
                    field_list.append(record.get_value())

            print(f'Bucket : {bucket},\nMeasurement : {measurement},\nField List : {field_list} \n')
        except Exception as e:
            raise Exception(e)

    def getDataFromMeasurement(self, bucket, measurement, query_condition):
        if self.influxdb_client is None:
            raise AttributeError('Please initInfluxDB function run!!')

        if not isinstance(query_condition, Dict):
            raise AttributeError('query_condition parameter type is dictionary')

        start_datetime = query_condition.get('start_datetime')
        end_datetime = query_condition.get('end_datetime')

        limit_count = query_condition.get('limit_count')
        field_list = query_condition.get('column_list')

        # range query 조건
        range_query = '|> range(start: {}, stop: {})'
        if start_datetime and end_datetime:
            if not re.match(self.datetime_pattern, start_datetime):
                raise AttributeError('start_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')
            if not re.match(self.datetime_pattern, end_datetime):
                raise AttributeError('end_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')

        if start_datetime and end_datetime:
            range_query = range_query.format(datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S').isoformat()+'Z', datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S').isoformat()+'Z')
        else:
            range_query = range_query.format('-30d', 'now()')

        # field query 조건
        field_query = None
        if field_list:
            field_query = '|> filter(fn:(r) => {})'
            field_query_or_condition = 'r._field == "{}"'
            fin_field_query_or_condition = ''

            for i in range(0, len(field_list)):
                fin_field_query_or_condition += field_query_or_condition.format(field_list[i])

                if len(field_list) - (i+1) >= 1:
                    fin_field_query_or_condition = fin_field_query_or_condition + ' or '
            field_query = field_query.format(fin_field_query_or_condition)

        timezone_kst = timezone(timedelta(hours=9))
        query_api = self.influxdb_client.query_api()

        # bucket, range 조건, measurement, field 조건, limit 조건
        query_str = 'from(bucket:"{0}") {1} |> filter(fn:(r) => r._measurement == "{2}") {3} |> limit(n:{4}) |> sort(columns: ["_time"], desc: true)'.format(
            bucket, range_query, measurement, field_query if field_query else '', limit_count if limit_count else 1000)

        result = query_api.query(org=self.influxOrganization, query=query_str)

        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_field(), record.get_value(), record.get_time().astimezone(timezone_kst)))
        
        df = pd.DataFrame(results, columns=['field', 'value', 'time'])

        print('Current project name: {} \n Current device name : {}\n'.format(self.currentProjectName, self.currentDevice))

        print('Data Preview \n')
        display(df.head())
        return df

    ###################################################### InfluxDB ######################################################

    ###################################################### TimescaleDB ######################################################

    def initTimeScaleDB(self, url):
        try:
            import sqlalchemy
            # self.timescaledb_conn = psycopg2.connect(url)
            engine = sqlalchemy.create_engine(url)
            self.timescaledb_conn = engine.connect()
            print('TimeScaleDB init Success!!')
        except Exception as e:
            raise Exception(e)

    def getTablesFromTimeScaleDBConn(self):
        if self.timescaledb_conn is None:
            raise AttributeError('Please initTimeScaleDB function run!!')

        try:
            target_database = self.timescaleDBUrl.split('/')[-1]  # 대상 데이터베이스 이름
            result = self.timescaledb_conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"))
            table_list = [row.table_name for row in result if row.table_name != 'spatial_ref_sys']  # 예외 처리를 통해 시스템 테이블 제외

            table_dict = {}
            table_dict[target_database] = table_list
        
            new_data = []
            for key, values in table_dict.items():
                for value in values:
                    new_data.append([key, value])
            
            df = pd.DataFrame(new_data, columns=['database', 'table'])
            return df
        except Exception as e:
            raise Exception(e)

    def showColumsFromTimeScaleDB(self, database, table):
        if self.timescaledb_conn is None:
            raise AttributeError('Please initTimeScaleDB function init!!')
    
        try:
            # cur = self.timescaledb_conn.cursor()
            results = self.timescaledb_conn.execute(text(f"SELECT * FROM information_schema.columns where table_catalog='{database}' and table_name='{table}';"))
            column_list = [row.column_name for row in results]
            print(f'Database : {database},\nCollection : {table},\nColumn List : {column_list} \n')
        except Exception as e:
            raise Exception(e)

    def getDataFromTimeScaleDB(self, database, table, query_condition):
        if self.timescaledb_conn is None:
            raise AttributeError('Please initTimeScaleDB function init!!')

        if not isinstance(query_condition, Dict):
            raise AttributeError('query_condition parameter type is dictionary')

        start_datetime = query_condition.get('start_datetime')
        end_datetime = query_condition.get('end_datetime')

        limit_count = query_condition.get('limit_count')
        field_list = query_condition.get('column_list')

        range_query = None
        if start_datetime and end_datetime:
            if not re.match(self.datetime_pattern, start_datetime):
                raise AttributeError('start_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')
            if not re.match(self.datetime_pattern, end_datetime):
                raise AttributeError('end_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')

        if start_datetime and end_datetime:
            range_query = "WHERE timestamp >= '{}' and timestamp <= '{}'".format(datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S'), datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S'))

        field_query = '*'
        if field_list:
            field_query = ','.join(field_list)

        try:
            query_result = self.timescaledb_conn.execute(text('SELECT {0} FROM {1}.public.{2} {3} LIMIT {4};'.format(field_query, database, table, range_query if range_query else '', limit_count if limit_count else 1000)))
            results = []
            for query in query_result:
                results.append(query)

            if field_list:
                df = pd.DataFrame(results, columns=field_list)
            else:
                column_results = self.timescaledb_conn.execute(text(f"SELECT * FROM information_schema.columns where table_catalog='{database}' and table_name='{table}';"))
                column_list = [row.column_name for row in column_results]
                df = pd.DataFrame(results, columns=column_list)

            print('Data Preview \n')
            display(df.head())
            return df
        except Exception as e:
            raise Exception(e)

    ###################################################### TimescaleDB ######################################################

    ###################################################### MongoDB ######################################################

    def initMongoDB(self, url):
        try:
            import pymongo
            self.mongodb_client = pymongo.MongoClient(url)
            print('MongoDB init Success!!')
        except Exception as e:
            raise Exception(e)

    def getCollectionsFromMongoDBClient(self):
        if self.mongodb_client is None:
            raise AttributeError('Please initMongoDB function run!!')

        database_list = self.mongodb_client.list_database_names()
        filtered_databases = [db for db in database_list if db not in ('admin', 'config', 'local')]

        database_dict = {}
        for db in filtered_databases:
            db_con = self.mongodb_client.get_database(db)
            database_dict[db] = db_con.list_collection_names()

        new_data = []
        for key, values in database_dict.items():
            for value in values:
                new_data.append([key, value])

        df = pd.DataFrame(new_data, columns=['database', 'collection'])
        return df

    def showColumnsFromMongoDBCollection(self, database, collection):
        if self.mongodb_client is None:
            raise AttributeError('Please initMongoDB function run!!')

        try:
            db = self.mongodb_client.get_database(database)
            collection = db.get_collection(collection)

            column_list = list(collection.find_one().keys())
            print(f'Database : {database},\nCollection : {collection.name},\nColumn List : {column_list} \n')
        except Exception as e:
            raise Exception(e)

    def getDataFromMongoDBClient(self, database, collection, query_condition):
        if self.mongodb_client is None:
            raise AttributeError('Please initMongoDB function run!!')

        if not isinstance(query_condition, Dict):
            raise AttributeError('query_condition parameter type is dictionary')

        start_datetime = query_condition.get('start_datetime')
        end_datetime = query_condition.get('end_datetime')

        limit_count = query_condition.get('limit_count')
        field_list = query_condition.get('column_list')

        range_query = None
        if start_datetime and end_datetime:
            if not re.match(self.datetime_pattern, start_datetime):
                raise AttributeError('start_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')
            if not re.match(self.datetime_pattern, end_datetime):
                raise AttributeError('end_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')

        if start_datetime and end_datetime:
            range_query = {'timestamp': {'$gt': datetime.strptime(start_datetime, '%Y-%m-%d %H:%M:%S'), '$lt': datetime.strptime(end_datetime, '%Y-%m-%d %H:%M:%S')}}

        field_query = {}
        if field_list:
            for field in field_list:
                field_query[field] = 1

        try:
            db = self.mongodb_client.get_database(database)
            collection = db.get_collection(collection)

            list_data = list(collection.find(range_query, field_query).limit(limit_count if limit_count else 1000))
            df = pd.DataFrame(list_data)

            print('Data Preview \n')
            display(df.head())
            return df

        except Exception as e:
            raise Exception(e)

    ###################################################### MongoDB ######################################################

    ###################################################### CassandraDB ######################################################

    def initCassandraDB(self, url, port, user, password):
        try:
            from cassandra.cluster import Cluster
            from cassandra.auth import PlainTextAuthProvider

            auth_provider = PlainTextAuthProvider(username=user, password=password)
            self.cassandra_cluster = Cluster([url], port=port, auth_provider=auth_provider)
            self.cassandra_keyspace = 'data_lake'
            print('CassandraDB init Success!!')
        except Exception as e:
            raise Exception(e)

    def getTablesFromCassandraCluster(self):
        try:
            keyspace_list = []
            session = self.cassandra_cluster.connect(self.cassandra_keyspace)

            keyspace_table_dict = {}
            for i in session.execute("SELECT * FROM system_schema.keyspaces;"): keyspace_list.append(i.keyspace_name) if i.keyspace_name.find('system') else None
            for keyspace in keyspace_list:
                t_list = []
                for i in session.execute("SELECT * FROM system_schema.tables WHERE keyspace_name = '{}';".format(keyspace)):
                    t_list.append(i.table_name)
                keyspace_table_dict[keyspace] = t_list

            new_data = []
            for key, values in keyspace_table_dict.items():
                for value in values:
                    new_data.append([key, value])
        
            df = pd.DataFrame(new_data, columns=['keyspace', 'table'])
        except Exception as error_msg:
            raise Exception(error_msg)
        finally:
            session.shutdown()
            return df

    def showColumnsFromCassandraCluster(self, keyspace, table):
        if self.cassandra_cluster is None:
            raise AttributeError('Please initCassandraDB function run!!')

        query = f"select * from system_schema.columns where keyspace_name='{keyspace}' and table_name='{table}';"
        session = self.cassandra_cluster.connect(self.cassandra_keyspace)
        column_list = []

        for row in session.execute(query):
            column_list.append(row.column_name)

        print(f'KeySpace : {keyspace}\nTable : {table}\nColumn List : {column_list}')

    def getDataFromCassandraCluster(self, keyspace, table, query_condition):
        if self.cassandra_cluster is None:
            raise AttributeError('Please initCassandraDB function run!!')

        if not isinstance(query_condition, Dict):
            raise AttributeError('query_condition parameter type is dictionary')

        query_str = 'SELECT {0} FROM {1}.{2} {3} LIMIT {4} ALLOW FILTERING'

        start_datetime = query_condition.get('start_datetime')
        end_datetime = query_condition.get('end_datetime')

        limit_count = query_condition.get('limit_count')
        column_list = query_condition.get('column_list')

        range_query = None
        if start_datetime and end_datetime:
            if not re.match(self.datetime_pattern, start_datetime):
                raise AttributeError('start_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')
            if not re.match(self.datetime_pattern, end_datetime):
                raise AttributeError('end_datetime pattern is wrong. pattern is "YYYY-MM-DD HH:mm:ss"')

            range_query = "WHERE timestamp >= '{}' and timestamp <= '{}'".format(start_datetime, end_datetime)

        column_query = ''
        if column_list:
            column_query = ','.join(column_list)
        else:
            column_query = '*'

        query_str = query_str.format(column_query, keyspace, table, range_query if range_query else '', limit_count if limit_count else 1000)
        
        def handle_page(page, results_list):
            for obj in page:
                result = process_row(obj)
                results_list.append(result)

        def process_row(user_row):
            result = []
            if column_list:
                for column in column_list:
                    if hasattr(user_row, column):
                        result.append(getattr(user_row, column))
            else:
                for key in user_row._fields:
                    result.append(getattr(user_row, key))

            return result

        results_list = []
        session = self.cassandra_cluster.connect(self.cassandra_keyspace)
        handler = PagedResultHandler(query_str, session, lambda page: handle_page(page, results_list))
        handler.finished_event.wait()

        if handler.error:
            raise handler.error

        if column_list:
            df = pd.DataFrame(results_list, columns=column_list)
        else:
            query = f"select * from {keyspace}.{table} limit 1;"
            query_column_list = []
            for row in session.execute(query):
                for f in row._fields:
                    query_column_list.append(f)

            df = pd.DataFrame(results_list, columns=query_column_list)
        
        print('Data Preview \n')
        display(df.head())
        return df


    ###################################################### CassandraDB ######################################################

    def exceptionHandle(self, responseData, subtype):
        resp_dict = json.loads(responseData.content)
        if subtype == "500":
            errFormat = {
                "timestamp": resp_dict['timestamp'],
                "code": responseData.status_code,
                "error": resp_dict['error'],
                "message": resp_dict['error']
            }
        else:
            errFormat = {
                "timestamp": resp_dict['timestamp'],
                "code": resp_dict['code'],
                "error": resp_dict['error'],
                "message": resp_dict['message']
            }
        
        raise Exception(f"Failed!!!\n {errFormat}")

    def checkStatusCode(self, status_code):
        """ Check status code and return 0 or 1. 
            CheckStatusCode.FAILED.value(0) is fail.
            CheckStatusCode.OK.value(1) is 200(OK).
            HTTPStatusCode.CREATED.value(2) is 201(Created).
            CheckStatusCode.NO_CONTENT.value(3) is 204(No Content).

        Args:
            data (Dict): Response of api
            status_code (Int): Status code of resource
        """
        if status_code == HTTPStatusCode.INTERNAL_SERVER_ERROR.value:
            return CheckStatusCode.FAILED.value, f"Internal Server Error!!!, Status: {status_code}"
        elif status_code == HTTPStatusCode.OK.value:
            return CheckStatusCode.OK.value, f"Ok!!!, Status: {status_code}"
        elif status_code == HTTPStatusCode.CREATED.value:
            return CheckStatusCode.CREATED.value, f"Created!!!, Status: {status_code}"
        elif status_code == HTTPStatusCode.NO_CONTENT.value:
            return CheckStatusCode.NO_CONTENT.value, f"No Content!!!, Status: {status_code}"
        else:
            return CheckStatusCode.FAILED.value, ""

    # 초기화
    def init(self):
        """ login of stackbase. 

        Raises:
            Exception: _description_
        """
        
        # userId = input("ID: ")
        # userPassword = getpass.getpass("PW: ")

        headers = {
            "Content-Type": "application/json",
            "X-NS": self.namespace
        }
        
        response = requests.request('post',f"{self.url}/internal/datalake/v1/auth", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        
        result = json.loads(response.content)

        self.organizationId = result['organizationId']
        self.id = result['id']
        self.email = result['email']
        self.name = result['name']
        self.minioBucket = result['minioBucket']
        self.minioAccessKey = result['minioAccessKey']
        self.minioSecretKey = result['minioSecretKey']

        self.currentProjectIdx = None
        self.currentProjectName = None
        self.currentDevice = None

        # git user.name, email 초기화(namespace, email)
        self.gitConfigInit()

        # minio init
        self.minioInit()

        print(returnMessage)

    def gitConfigInit(self):
        response = requests.request('GET', f"{self.giteamanager_url}/stackbase/v1/gitea-manager/users/{self.minioBucket}")

        if response.status_code == HTTPStatusCode.OK.value:
            print(f'set git config username: {self.minioBucket}, email: {self.email}')
            os.system(f'git config --global user.name {self.minioBucket}')
            os.system(f'git config --global user.email {self.email}')
            os.system(f'git config --global credential.helper store')
            os.system('git config --global init.defaultBranch main')
        else:
            os.system(f'git config --global --unset user.name')
            os.system(f'git config --global --unset user.email')
            os.system('git config --global init.defaultBranch main')
            print('git config user.name and user.email are replaced with user from the OS system.')

    def minioInit(self):
        try:
            import boto3
            self.minio_client = boto3.client('s3', endpoint_url=self.minio_url, aws_access_key_id=self.minioAccessKey, aws_secret_access_key=self.minioSecretKey)
            print('MinIO init Success!!')
        except Exception as e:
            raise Exception(e)
    
    def minioFileObjUpload(self, local_path, bucket_name):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')

        if os.path.exists(local_path):
            file_name = local_path.split('/')[-1]

            try:
                with open(local_path, 'rb') as data:
                    self.minio_client.upload_fileobj(data, bucket_name, file_name)
                    print(f'Minio Upload Success!, Status: {HTTPStatusCode.OK.value}')
            except botocore.exceptions.ClientError as clientError:
                raise clientError
            except Exception as e:
                raise e
        else:
            raise FileNotFoundError(f'File {local_path} does not Exists')

    def minioFileDownload(self, bucket_name, object_key, local_path):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')

        try:
            with open(local_path, 'wb') as data:
                print(f'{object_key} in {bucket_name} download start ...')
                self.minio_client.download_fileobj(Bucket=bucket_name, Key=object_key, Fileobj=data)
                print(f'{object_key} in {bucket_name} download completed!, save path: {local_path}')
        except botocore.exceptions.ClientError as clientError:
            raise clientError
        except Exception as e:
            raise e

    def minioListObjects(self, bucket_name):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')

        try:
            paginator = self.minio_client.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(Bucket=bucket_name)
            timezone_kst = timezone(timedelta(hours=9))

            results = []
            for page in page_iterator:
                contents = page.get('Contents')

                if contents:
                    for keys in contents:
                        results.append((keys['Key'], keys['Size'], keys['LastModified'].astimezone(timezone_kst).strftime('%Y/%m/%d %H:%M:%S')))
            objects_df = pd.DataFrame(results, columns=['file_name', 'size(Bytes)', 'time'])
            return objects_df
        except botocore.exceptions.ClientError as clientError:
            raise clientError
        except botocore.exceptions.NoCredentialsError as noCredentialsError:
            raise noCredentialsError
        except Exception as e:
            raise e
    
    def minioGetObject(self, bucket_name, file_name):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')

        try:
            response = self.minio_client.get_object(Bucket=bucket_name, Key=file_name)
            meta_data = response.get('ResponseMetadata')

            if meta_data.get('HTTPStatusCode') == HTTPStatusCode.OK.value:
                return HTTPStatusCode.OK.value            
        except botocore.exceptions.ClientError as clientError:
            if clientError.response['Error']['Code'] == 'NoSuchKey':
                raise FileNotFoundError(f'No Such File : {file_name}')

            raise clientError
        except Exception as e:
            raise e

    def minioDeleteObject(self, bucket_name, file_name):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')

        try:
            get_object_status = self.minioGetObject(bucket_name=bucket_name, file_name=file_name)

            if get_object_status == HTTPStatusCode.OK.value:
                print(f'{file_name} Deleteing in {bucket_name}')
                self.minio_client.delete_object(Bucket=bucket_name, Key=file_name)
            else:
                raise FileExistsError(f'{file_name} not exists in MinIO {bucket_name}')

        except botocore.exceptions.ClientError as clientError:
            raise clientError
        except botocore.exceptions.NoCredentialsError as noCredentialsError:
            raise noCredentialsError
        except Exception as e:
            raise e

    def minioCreateBucket(self, bucket_name):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')
        
        try:
            response = self.minio_client.create_bucket(Bucket=bucket_name)

            response_data = response.get('ResponseMetadata')
            if response_data.get('HTTPStatusCode') == HTTPStatusCode.OK.value:
                location = response.get('Location')
                print(f'{bucket_name} is created. MinIO location : {location}')

        except botocore.exceptions.ClientError as clientError:
            raise clientError
        except botocore.exceptions.BucketAlreadyOwnedByYou as ownedError:
            raise ownedError(f'{bucket_name} is you already own it!')
        except botocore.exceptions.BucketAlreadyExists as existsBucket:
            raise existsBucket(f'{bucket_name} already exists!')
        except Exception as e:
            raise e
    
    def minioDeleteBucket(self, bucket_name):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')

        try:
            # bucket 명이 user명 동일
            print(f'{bucket_name} Deleting..')
            response = self.minio_client.delete_bucket(Bucket=bucket_name, ExpectedBucketOwner=self.minioBucket)
            response_data = response.get('ResponseMetadata')

            if response_data.get('HTTPStatusCode') == HTTPStatusCode.NO_CONTENT.value:
                print(f'{bucket_name} is deleted')
        except botocore.exceptions.ClientError as clientError:
            raise clientError
        except Exception as e:
            raise e

    def minioUserBucketList(self):
        if self.minio_client is None:
            raise AttributeError('Please MinIO Client Init!!')

        try:
            response = self.minio_client.list_buckets()
            response_data = response.get('ResponseMetadata')
            timezone_kst = timezone(timedelta(hours=9))

            if response_data.get('HTTPStatusCode') == HTTPStatusCode.OK.value:
                bucket_list = response.get('Buckets')

                results = []
                for bucket in bucket_list:
                    results.append((bucket['Name'], bucket['CreationDate'].astimezone(timezone_kst).strftime('%Y/%m/%d %H:%M:%S')))

                df = pd.DataFrame(results, columns=['bucket_name', 'created_at'])
                return df
        except botocore.exceptions.ClientError as clientError:
            raise clientError
        except Exception as e:
            raise e

    def setDevice(self, assetCode):
        headers = {
            "Content-Type": "application/json",
            "X-ORG-CODE": self.organizationId
        }

        # projectDataFrame에서 idx로 projectCode 가져오기
        projectCode, _ = self.getProjectCodeByIdx(self.currentProjectIdx, self.projectDataFrame)

        response = requests.request('get',f"{self.url}/internal/datalake/v1/projects/{projectCode}/assets/{assetCode}", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == 0:
            self.exceptionHandle(response, returnMessage)
        
        result = json.loads(response.content)

        # TODO: Device 별 database 접속정보 조회가 가능하면 DB별로 변수 받을수 있게 변경
        self.influxUrl = result['url']
        self.influxOrganization = result['organization']
        self.influxToken = result['token']
        self.influxBucket = result['bucket']
        self.influxMeasurement = result['measurement']
        self.currentDevice = assetCode

        print('Current project name: {} \n Current device name : {}'.format(self.currentProjectName, self.currentDevice))

        print(f"[INFO] List of accessible DBs: InfluxDB")

    # 유저의 프로젝트 리스트 조회
    def getProject(self):
        """ Print list of project in sdt cloud

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        headers = {
            "Content-Type": "application/json",
            "X-ORG-CODE": self.organizationId
        }

        response = requests.request('get',f"{self.url}/internal/datalake/v1/projects", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == CheckStatusCode.FAILED.value:
            self.exceptionHandle(response, returnMessage)
        elif respStatus == CheckStatusCode.NO_CONTENT.value:
            print(returnMessage)
            return 0

        result = json.loads(response.content)
        self.projectDataFrame = pd.DataFrame(result)
        
        print(returnMessage)
        
        return self.projectDataFrame

    def getProjectCodeByIdx(self, idx, df):
        """
            ProjectDataFrame에서 index로 project code 조회
        Args:
            idx (int): dataframe idx
            df (pd.DataFrame): project dataframe

        Returns:
            str: projectCode
        """        
        if df is not None and df.empty != True:
            return df.iloc[idx]['code'], df.iloc[idx]['name']

    # 프로젝트 선택
    def setProject(self, idx):
        """
            idx로 projectCode 조회하여 project에 속한 AssetData 가져오기
        Args:
            idx (_type_): project dataframe index

        Returns:
            _type_: _description_
        """

        headers = {
            "Content-Type": "application/json",
            "X-ORG-CODE": self.organizationId
        }

        # projectDataFrame에서 idx로 projectCode 가져오기
        projectCode, projectName = self.getProjectCodeByIdx(idx, self.projectDataFrame)

        response = requests.request('get',f"{self.url}/internal/datalake/v1/projects/{projectCode}/assets", headers=headers)
        respStatus, returnMessage = self.checkStatusCode(response.status_code)

        if respStatus == CheckStatusCode.FAILED.value:
            self.exceptionHandle(response, returnMessage)

        result = json.loads(response.content)
        self.assetDataFrame = pd.DataFrame(result)

        # 현재 선택한 프로젝트
        self.currentProjectIdx = idx
        self.currentProjectName = projectName

        # 현재 선택한 device는 무조건 초기화
        self.currentDevice = None

        print('Current project name: {} \n'.format(self.currentProjectName))

        print(returnMessage)
        return self.assetDataFrame


    def getUserRepository(self):
        headers = {
            'email': self.email
        }

        response = requests.request('GET',f"{self.giteamanager_url}/stackbase/v1/gitea-manager/repos", headers=headers)

        if response.status_code == HTTPStatusCode.OK.value:
            repository_list = response.json().get('content')

            results = []
            if len(repository_list) > 0:
                for repo in repository_list:
                    results.append((repo.get('name'), repo.get('default_branch'), repo.get('clone_url')))

                df = pd.DataFrame(results, columns=['repository_name', 'branch', 'clone_url'])
                pd.set_option('display.max_colwidth', None)
                # df = df.style.format({'clone_url': self._make_clickable_url})
                html = df.to_html(render_links=True, escape=False)
                display(HTML(html))
            else:
                print('User Repository Does Not Exists')
        else:
            return f'Failed!, Status: {response.status_code}, Message: {response.json()}'

    def getPublicRepository(self):
        response = requests.request('GET', f'{self.giteamanager_url}/stackbase/v1/gitea-manager/repos/all')
        
        if response.status_code == HTTPStatusCode.OK.value:
            repository_list = response.json().get('content')
            
            results = []
            if len(repository_list) > 0:
                for repo in repository_list:
                    results.append((repo.get('name'), repo.get('owner').get('email'), repo.get('default_branch'), repo.get('clone_url')))
                    
                df = pd.DataFrame(results, columns=['repository_name', 'owner_email', 'branch', 'clone_url'])
                pd.set_option('display.max_colwidth', None)
                # df = df.style.format({'clone_url': self._make_clickable_url})
                # df = df.style.format({'clone_url': self._make_clickable_url}, escape='html')
                html = df.to_html(render_links=True, escape=False)
                display(HTML(html))
            else:
                print('Repository List Does Not Exists')
        else:
            return f'Failed!, Status: {response.status_code}, Message: {response.json()}'

    def checkGiteaUrlRegex(self, url):
        pattern = re.compile(self.giteamanager_url_regex, re.IGNORECASE)
        result = pattern.match(url)
        
        if result:
            print('repository url verify!')
            return result.lastindex
        else:
            print('respotiroy url is not verify!')
            return 0

    def gitRepoInitFolder(self, path='.'):
        try:
            if path == '.':
                result = os.system('git init')
            else:
                if os.path.exists(path):
                    if os.path.isdir(path):
                        os.chdir(path)
                        result = os.system('git init')
                    else:
                        raise AttributeError(f'{path} is not directory!')
                else:
                    raise FileNotFoundError(f'{path} does not Exists')

            if result == 0:
                print('git Init Complete')
                return HTTPStatusCode.OK.value
        except Exception as e:
            raise Exception(e)

    def gitRepoAddRemoteUrl(self, remote_url, path='.'):
        try:
            remote_ref = os.popen('git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null').read()

            if remote_ref == '':
                if path == '.':
                    result = os.system(f'git remote add --track main origin {remote_url}')
                else:
                    if os.path.exists(path):
                        if os.path.isdir(path):
                            os.chdir(path)
                            result = os.system(f'git remote add --track main origin {remote_url}')
                        else:
                            raise AttributeError(f'{path} is not directory!')
                    else:
                        raise FileNotFoundError(f'{path} does not Exists')

                if result == 0:
                    print('git remote_url add success!')
                    return HTTPStatusCode.OK.value
            else:
                print('remote_url already exists!')
                return HTTPStatusCode.NO_CONTENT.value
        except Exception as e:
            raise Exception(e)

    def cloneUserRepository(self, clone_url):
        try:
            if clone_url != '':
                regex_result = self.checkGiteaUrlRegex(clone_url)
                if regex_result > 0:
                    result = os.system(f'git clone {clone_url}')

                    if result == 0:
                        repository_name = clone_url.split('/')[len(clone_url.split('/')) - 1].split('.')[0]

                        os.chdir(f'./{repository_name}')  # change directory
                        print(f'Completed Clone Repository!, Status: {HTTPStatusCode.OK.value}')
                        return HTTPStatusCode.OK.value
                    else:
                        print(f'Failed Clone Repository!, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
                        return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def addStageFile(self, file_path_for_add_stages='.'):
        try:
            file_list = ' '.join(file_path_for_add_stages.split(','))
            result = os.system(f'git add {file_list}')

            if result == 0:
                print('Completed! Add File to Stage')
                return HTTPStatusCode.OK.value
            else:
                print('Failed! Add File to Stage')
                return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def restoreStagedFile(self, file_path_for_restore_stages):
        try:
            file_list = ' '.join(file_path_for_restore_stages.split(','))
            result = os.system(f'git restore --staged {file_list}')

            if result == 0:
                print('Completed! Restore File')
                return HTTPStatusCode.OK.value
            else:
                print('Failed! Restore File')
                return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def commitRepository(self, commit_message):
        try:
            result = os.system(f'git commit -m "{commit_message}"')

            if result == 0:
                print('Commit Completed!')
                return HTTPStatusCode.OK.value
            else:
                print('Commit Failed!')
                return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def pushRepository(self, push_file_path='.'):
        try:
            headers = {'email': self.email}
            response = requests.get(f"{self.giteamanager_url}/stackbase/v1/gitea-manager/users/me", headers=headers)
            
            if response.status_code == HTTPStatusCode.OK.value:
                access_token = response.json().get('accessToken')

                remote_push_url = os.popen('git config --get remote.origin.url').read().replace('\n', '')

                if self.checkGiteaUrlRegex(remote_push_url) > 0:
                    result = None
                    remote_push_url = remote_push_url.replace('http://', '')

                    # http://{username}:{access_token}@{gitea ip}/{username}/{repository_name}.git (self.minioBucket : giteamanager 내 username과 동일)

                    if push_file_path == '.':
                        result = os.system(f'git push http://{self.minioBucket}:{access_token}@{remote_push_url}')
                    else:
                        os.chdir(f'./{push_file_path}')
                        result = os.system(f'git push http://{self.minioBucket}:{access_token}@{remote_push_url}')

                    if result == 0:
                        print('Push Completed!')
                        return HTTPStatusCode.OK.value
                    else:
                        print('Push Failed!')
                        return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
                else:
                    raise AttributeError('Not added remote_url this path!')
            else:
                raise AttributeError('gitea access_token not exists!')
        except Exception as e:
            raise Exception(e)

    def pullRepository(self, repository_url):
        try:
            regex_result = self.checkGiteaUrlRegex(repository_url)

            if regex_result > 0:
                repository_name = repository_url.split('/')[len(repository_url.split('/')) - 1].split('.')[0]
                if os.path.exists(f'./{repository_name}'):
                    os.chdir(f'./{repository_name}')  # repository 폴더로 이동

                    result = os.system(f'git pull {repository_url} --allow-unrelated-histories')
                    if result == 0:
                        print(f'Completed! Pull Repository: {repository_url}')
                        return HTTPStatusCode.OK.value
                    else:
                        os.chdir('..')  # 상위 디렉토리로 이동
                        print(f'Failed! Pull Repository: {repository_url}')
                        return HTTPStatusCode.INTERNAL_SERVER_ERROR.value
                else:
                    print('repository path does not exist in notebook file path \n')
                    clone_repository_status = self.cloneUserRepository(repository_url)
                    return clone_repository_status
        except Exception as e:
            print(f'Error Raise! Reason: {e}, Status: {HTTPStatusCode.INTERNAL_SERVER_ERROR.value}')
            return HTTPStatusCode.INTERNAL_SERVER_ERROR.value

    def createRepository(self, repo_name, private_flag=True):
        try:
            headers = {'email': self.email}
            data = {
                "name": repo_name,
                "auto_init": False,
                "description": "",
                "gitignores": "",
                "issue_labels": "",
                "license": "",
                "private": True if private_flag else False,
                "readme": "Default",
                "template": False,
                "trust_model": "default"
            }

            response = requests.post(f"{self.giteamanager_url}/stackbase/v1/gitea-manager/repos", headers=headers, data=json.dumps(data))

            if response.status_code == HTTPStatusCode.CREATED.value:
                print('Repository Create Success! \n')
                response_data = response.json()
                return response_data.get('clone_url')
            elif response.status_code == HTTPStatusCode.CONFLICT.value:
                raise Exception(f'{repo_name} is conflict!')
            else:
                raise Exception(f'API Error Status : {response.status_code}')

        except Exception as e:
            raise Exception(e)

    # # 폴더 등록
    # def create_folder(self, storageId, parentId, dirName):
    #     """ Create folder in stackbase's storage

    #     Args:
    #         storageId (Str): Storage ID that create folder.
    #         parentId (Str): Folder ID that create folder. If you want to set root path, you have to enter "".
    #         dirName (Str): Folder name.

    #     Raises:
    #         Exception: _description_

    #     Returns:
    #         _type_: _description_
    #     """
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": self.userToken
    #     }

    #     bodys = json.dumps({
    #         "parentId": parentId,
    #         "name": dirName,
    #         "storageId": storageId
    #     })

    #     response = requests.request('post',f"{self.url}/stackbase/v1/folder", headers=headers, data=bodys)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)

    #     result = json.loads(response.content)
    #     result['createdAt'] = datetime.fromtimestamp(int(result['createdAt']/1000), timezone(timedelta(hours=9)))
        
    #     print(returnMessage)
    
    # # 트리 검색
    # def get_tree(self, storageId, parentId):
    #     """ Print list of tree in stackbase.

    #     Args:
    #         storageId (Str): Storage ID
    #         parentId (Str): Folder ID. If you want to set root path, you have to enter "".

    #     Raises:
    #         Exception: _description_

    #     Returns:
    #         _type_: _description_
    #     """
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": self.userToken
    #     }

    #     param = {
    #         "storageId": storageId,
    #         "parentId": parentId
    #     }

    #     response = requests.request('get',f"{self.url}/stackbase/v1/trees", headers=headers, params=param)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)
    #     elif respStatus == 3:
    #         print(returnMessage)
    #         return 0
            
    #     result = json.loads(response.content)
    #     df1 = pd.DataFrame(result)
    #     df2 = pd.DataFrame(result['trees'])
        
    #     df = pd.concat([df1.drop(['trees'], axis=1), df2], axis=1)
    #     for n in range(len(df)):
    #         df.loc[n, 'modifiedAt'] = datetime.fromtimestamp(int(df.loc[n, 'modifiedAt']/1000), timezone(timedelta(hours=9)))
        
    #     print(returnMessage)
    #     return df

    # # 폴더 수정
    # def update_folder(self):
    #     print("update")

    # # 폴더 삭제
    # def delete_folder(self):
    #     print("delete")

    # # 컨텐츠 조회
    # def get_content(self):
    #     print("get")

    # # 컨텐츠 수정
    # def update_content(self):
    #     print("test")
    
    # # 컨텐츠 삭제
    # def delete_content(self):
    #     print("test")

    # # 컨텐츠 다운로드
    # def fget_content(self, fileId, getPath):
    #     """ Download content(file) from stackbase.

    #     Args:
    #         fileId (Str): File ID
    #         getPath (Str): File save path.

    #     Raises:
    #         Exception: _description_
    #     """
    #     headers = {
    #         "Authorization": self.userToken
    #     }

    #     response = requests.request('get',f"{self.url}/stackbase/v1/contents/download/{fileId}", headers=headers)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)
        
    #     with open(getPath, "wb") as f:
    #         f.write(response.content)
        
    #     print(returnMessage)
    
    # # 컨텐츠 등록
    # def fput_content(self, storageId, folderId, filePath, fileVersion, fileFormat, fileTag):
    #     """ Upload content(file) in stackbase

    #     Args:
    #         storageId (Str): Storage ID
    #         folderId (Str): Folder ID
    #         filePath (Str): Path of upload file
    #         fileVersion (Str): Version of file
    #         fileFormat (Str): Format of file
    #         fileTag (Str): Tag of file

    #     Raises:
    #         Exception: _description_

    #     Returns:
    #         _type_: _description_
    #     """
    #     headers = {
    #         "Authorization": self.userToken
    #     }

    #     bodys = json.dumps({
    #         "storageId": storageId,
    #         "folderId": folderId,
    #         "version": fileVersion,
    #         "format": fileFormat,
    #         "tag": fileTag
    #     })

    #     file_open = open(filePath, 'rb')

    #     files={
    #         'request': (None, bodys, 'application/json'),
    #         "content": (filePath.split("/")[-1], file_open, 'application/octet-stream')
    #     }

    #     response = requests.request("POST", f"{self.url}/stackbase/v1/contents", headers=headers, files=files)
    #     respStatus, returnMessage = self.checkStatusCode(response.status_code)

    #     if respStatus == 0:
    #         self.exceptionHandle(response, returnMessage)

    #     result = json.loads(response.content)
    #     result['createdAt'] = datetime.fromtimestamp(int(result['createdAt']/1000), timezone(timedelta(hours=9)))
    #     result['modifiedAt'] = datetime.fromtimestamp(int(result['modifiedAt']/1000), timezone(timedelta(hours=9)))
        
    #     print(returnMessage)