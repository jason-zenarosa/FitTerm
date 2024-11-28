from datetime import datetime

class NutritionEntry:
    def __init__(self, associated_user:str, id:int, name:str, timestamp:datetime, calories:int):
        self.associated_user = associated_user
        self.id = id
        self.name = name
        self.timestamp = timestamp
        self.calories = calories

    def __str__(self):
        return f"'{self.associated_user}', '{self.name}', '{self.timestamp}', '{self.calories}'"
