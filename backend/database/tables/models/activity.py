from datetime import datetime

class Activity:
    def __init__(self, associated_user:str, id:int, name:str, description:str, timestamp:datetime, completion:bool):
        self.associated_user = associated_user
        self.id = id
        self.name = name
        self.description = description
        self.timestamp = timestamp
        self.completion = completion

    def __str__(self):
        return f"'{self.associated_user}', '{self.name}', '{self.description}', '{self.timestamp}', '{self.completion}'"