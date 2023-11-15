from abc import ABC, abstractmethod


class BaseDBConnection(ABC):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    @abstractmethod
    def connect(self):
        """Establishes a connection to the database."""
        pass

    @abstractmethod
    def disconnect(self):
        """Closes the database connection."""
        pass

    @abstractmethod
    def execute_query(self, query, fetch_results=True):
        """Executes a single query."""
        pass


class BaseDBConnectionAsync(ABC):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None

    @abstractmethod
    def connect_async(self):
        pass

    @abstractmethod
    def disconnect_async(self):
        """Closes the database connection."""
        pass

    @abstractmethod
    def execute_query_async(self, query, fetch_results=True):
        """Executes a single asynchronous query."""
        pass
