from sqlite3 import Connection

class DatabaseTable:
    def __init__(self, connection:Connection):
        self.connection = connection

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        return results

    def execute_nonquery(self, command):
        cursor = self.connection.cursor()
        cursor.execute(command)
        self.connection.commit()
        cursor.close()
        