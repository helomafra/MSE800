import sqlite3

# Singleton class for database connections
class DatabaseSingleton:
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get_connection(self):
        # Get or create a persistent connection
        if self._connection is None:
            self._connection = sqlite3.connect("app.db")
        return self._connection
    
    def close_connection(self):
        # Close the persistent connection
        if self._connection:
            self._connection.close()
            self._connection = None
    
    def create_connection(self):
        # Create a new connection (for compatibility)
        return sqlite3.connect("app.db")

# Global instance of singleton
db = DatabaseSingleton()
