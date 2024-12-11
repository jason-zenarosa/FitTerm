from datetime import datetime

class NutritionEntry:
    def __init__(self, associated_user:str, id:int, name:str, timestamp:datetime | str, calories:int):
        self.associated_user = associated_user
        self.id = id
        self.name = name
        if (type(timestamp) == datetime):
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        self.calories = calories

    def __str__(self):
        return f"'{self.associated_user}', '{self.name}', '{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}', {self.calories}"
