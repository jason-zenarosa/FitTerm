import sqlite3

# Connect to the database (or create it if it doesn't exist)
connection = sqlite3.connect('FitTerm.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        username    TEXT PRIMARY KEY,
        password    TEXT NOT NULL
    )
''')

# Create the Activities table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Activities (
        associated_user     TEXT,
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        name                TEXT NOT NULL,
        description         TEXT,
        timestamp           DATETIME,
        completion          BOOLEAN,
        FOREIGN KEY (associated_user) REFERENCES Users(username)
    )
''')

# Create the Nutrition Entry table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS NutritionEntries (
        associated_user     TEXT,
        id                  INTEGER PRIMARY KEY AUTOINCREMENT,
        name                TEXT NOT NULL,
        timestamp           DATETIME,
        calories            INTEGER,
        FOREIGN KEY (associated_user) REFERENCES Users(username)
    )
''')

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
