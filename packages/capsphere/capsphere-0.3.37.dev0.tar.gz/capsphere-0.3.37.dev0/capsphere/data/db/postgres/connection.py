import logging
import os
import psycopg

from contextlib import contextmanager
from psycopg import OperationalError
from capsphere.data.db.exception import DatabaseExecutionError, DatabaseConnectionError
from capsphere.data.db.interface import BaseDBConnection, BaseDBConnectionAsync
from capsphere.data.db.postgres.utils import build_connection_args
from capsphere.data.db.utils import check_env_vars


class Connector(BaseDBConnection):
    def __init__(self, ssl_cert_path=None):
        self.logger = logging.getLogger(__name__)

        check_env_vars(['DB_HOST', 'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_PORT'], self.logger)

        super().__init__(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=int(os.getenv('DB_PORT', 5432))
        )
        self.ssl_cert_path = ssl_cert_path

    @contextmanager
    def get_connection(self):
        self.connect()
        try:
            yield self
        finally:
            self.disconnect()

    def connect(self):
        """
        Establishes a connection to the database.
        """
        if not self.connection:
            try:
                connection_args = build_connection_args(self.host, self.database, self.user, self.password, self.port,
                                                        self.ssl_cert_path)
                self.connection = psycopg.connect(**connection_args)
            except OperationalError as e:
                raise DatabaseConnectionError(e)

    def disconnect(self):
        """
        Closes the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, query, params=None, fetch_results=True):
        """
        Executes a single query with parameters.
        """
        if not self.connection:
            raise DatabaseConnectionError("Not connected to the database.")

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)  # Pass the parameters to the cursor
                if fetch_results:
                    headers = [desc[0] for desc in cursor.description]
                    result = cursor.fetchall()
                    return result, headers
                else:
                    self.connection.commit()
        except Exception as e:
            raise DatabaseExecutionError(f"Error executing query: {e}")


class ConnectorAsync(BaseDBConnectionAsync):
    def __init__(self, ssl_cert_path=None):
        self.logger = logging.getLogger(__name__)

        check_env_vars(['DB_HOST', 'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_PORT'], self.logger)

        super().__init__(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=int(os.getenv('DB_PORT', 5432))
        )
        self.ssl_cert_path = ssl_cert_path

    async def ensure_connection(self):
        """
        Ensure that the database connection is established.
        """
        if not self.connection:
            await self.connect_async()

    @contextmanager
    def get_connection(self):
        self.connect_async()
        try:
            yield self
        finally:
            self.disconnect_async()

    async def connect_async(self):
        """
        Establishes an asynchronous connection to the database.
        """
        if not self.connection:
            try:
                connection_args = build_connection_args(self.host, self.database, self.user, self.password, self.port,
                                                        self.ssl_cert_path)
                self.connection = await psycopg.AsyncConnection.connect(**connection_args)
            except OperationalError as e:
                raise DatabaseConnectionError(e)

    async def disconnect_async(self):
        """
        Closes the asynchronous database connection.
        """
        if self.connection:
            await self.connection.close()
            self.connection = None

    async def execute_query_async(self, query, params=None, fetch_results=True):
        """
        Executes a single asynchronous query.
        """
        if not self.connection:
            raise DatabaseConnectionError("Not connected to the database.")

        try:
            async with self.connection.cursor() as cursor:
                await cursor.execute(query, params)
                if fetch_results:
                    headers = [desc[0] for desc in cursor.description]
                    result = cursor.fetchall()
                    return result, headers
                else:
                    await self.connection.commit()
        except Exception as e:
            raise DatabaseExecutionError(f"Error executing query: {e}")
