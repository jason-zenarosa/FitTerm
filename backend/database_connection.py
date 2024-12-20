import sqlite3
from database.tables.user_table import UserTable
from database.tables.activity_table import ActivityTable
from database.tables.nutrition_table import NutritionTable

class DatabaseConnection:
    def __init__(self, connection_string):
        self.connection = sqlite3.connect(connection_string)
        self.user_table = UserTable(self.connection)
        self.activity_table = ActivityTable(self.connection)
        self.nutrition_table = NutritionTable(self.connection)
        
    def close(self):
        self.connection.close()
