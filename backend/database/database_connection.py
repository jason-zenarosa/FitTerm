import sqlite3

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection = sqlite3.connect(connection_string)
    
    