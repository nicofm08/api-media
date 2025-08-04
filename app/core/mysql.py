"""This module contains MySQLClient for connecting to the MySQL database and executing queries."""

import mysql.connector
from mysql.connector import Error
from app.core.logger_custom import log
from app.core.constants import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_DATABASE,
    LOG_CORE,
    LOG_FINERROR,
)

class MySQLClient:
    """Class for connecting to the MySQL database and interacting with it."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MySQLClient, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.host = MYSQL_HOST
            self.user = MYSQL_USER
            self.password = MYSQL_PASSWORD
            self.database = MYSQL_DATABASE
            self.connection = None
            self.cursor = None
            self.connect()
            self.initialized = True

    def connect(self, db=None):
        """Connect to the MySQL database."""
        try:
            if self.connection is None or not self.connection.is_connected():
                if not db:
                    db = self.database
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    db=db,
                    charset="utf8mb4",
                    collation="utf8mb4_unicode_ci",
                )
                self.cursor = self.connection.cursor(dictionary=False)
                log.info(f"{LOG_CORE} Connected to database: {db}")
        except Error as err:
            log.error(f"{LOG_FINERROR} Can't connect to the database: {err}")
            self.connection = None

    def disconnect(self):
        """Disconnect from the MySQL database."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        self.connection = None

    def reconnect(self):
        """Reconnect to the MySQL database."""
        self.disconnect()
        self.connect()
        log.info(f"{LOG_CORE} Database reconnected")

    async def add_update(self, query, db=None):
        """Execute an insert or update query."""
        try:
            self.connect(db=db)
            self.cursor.execute(query)
            self.connection.commit()
            if self.cursor.lastrowid:  # Si lastrowid tiene valor, fue una inserción
                result = self.cursor.lastrowid
                log.info(f"{LOG_CORE} The query add_update was executed successfully, last inserted id: {result}")
            else:  # Si lastrowid no tiene valor, fue una actualización
                result = self.cursor.rowcount
                log.info(f"{LOG_CORE} The query add_update was executed successfully, rows affected: {result}")
            return result
        except mysql.connector.Error as err:
            log.error(f"{LOG_FINERROR} The query could not be executed: {err}")
            return None

    async def read(self, query, db=None):
        """Execute a read query."""
        try:
            self.connect(db=db)
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            log.info(f"{LOG_CORE} The query read was executed successfully")
            return results
        except mysql.connector.Error as err:
            log.error(f"{LOG_FINERROR} The query could not be executed: {err}")
            return None

    async def read_columns(self, query, db=None):
        """Execute a read query and return a list of dictionaries."""
        try:
            self.connect(db=db)
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            column_names = [column[0] for column in cursor.description]
            formatted_results = []
            for row in results:
                formatted_row = {column_names[i]: value for i, value in enumerate(row)}
                formatted_results.append(formatted_row)
            log.info(f"{LOG_CORE} The query read_columns was executed successfully")
            return formatted_results
        except mysql.connector.Error as err:
            log.error(f"{LOG_FINERROR} The query could not be executed: {err}")
            return None

    def __del__(self):
        self.disconnect()
