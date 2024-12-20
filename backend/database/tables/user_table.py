from database.tables.models.user import User
from database.tables.database_table import DatabaseTable

class UserTable(DatabaseTable):
    
    def get_user(self, username) -> User | None:
        results = self.execute_query(f"SELECT * FROM Users WHERE username = '{username}'")
        if len(results) == 0:
            return None
        user = results[0]
        
        return User(*user)
    
    def add_user(self, username, password):
        user = User(username, password)
        self.execute_nonquery(f"""
            INSERT INTO Users (username, password)
            VALUES ({user})                 
        """)
