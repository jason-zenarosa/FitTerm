from database.tables.models.activity import Activity
from database.tables.database_table import DatabaseTable

class ActivityTable(DatabaseTable):

    def get_activities(self, username:str) -> list[Activity]:
        results = self.execute_query(f"SELECT * FROM Activities WHERE associated_user = '{username}'")
        activity_list = []
        for row in results:
            new_activity = Activity(*row)
            activity_list.append(new_activity)

        return activity_list
    
    def add_activity(self, activity:Activity):
        self.execute_nonquery(f"""
            INSERT INTO Activities (associated_user, name, description, timestamp, completion)
            VALUES ({activity})
        """)
