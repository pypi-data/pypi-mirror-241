from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra.auth import PlainTextAuthProvider
from threading import Event


class PagedResultHandler:
    def __init__(self, query, session, handler=None):
        self.error = None
        self.finished_event = Event()
        statement = SimpleStatement(query, fetch_size=500)
        future = session.execute_async(statement)
        self.future = future
        self.query = query
        self.handler = handler
        self.future.add_callbacks(
            callback=self.handle_page,
            errback=self.handle_error)

    def handle_page(self, rows):
        if not self.handler:
            raise RuntimeError('A page handler function was not defined for the query')
        self.handler(rows)

        if self.future.has_more_pages:
            self.future.start_fetching_next_page()
        else:
            self.finished_event.set()

    def handle_error(self, exc):
        self.error = exc
        self.finished_event.set()
