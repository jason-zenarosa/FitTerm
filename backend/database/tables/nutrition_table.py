from database.tables.models.nutrition_entry import NutritionEntry
from database.tables.database_table import DatabaseTable

class NutritionTable(DatabaseTable):

    def get_nutrition_entries(self, username):
        results = self.execute_query(f"SELECT * FROM NutritionEntries WHERE associated_user = '{username}'")
        nutrition_list = []
        for row in results:
            new_nutrition_entry = NutritionEntry(*row)
            nutrition_list.append(new_nutrition_entry)

        return nutrition_list
    
    def add_activity(self, nutrition_entry:NutritionEntry):
        self.execute_nonquery(f"""
            INSERT INTO NutritionEntries (associated_user, name, timestamp, calories)
            VALUES ({nutrition_entry})
        """)
