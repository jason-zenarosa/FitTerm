class User:
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.username}, {self.password}"

    def verify_password(self, password:str):
        return self.password == password
