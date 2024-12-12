# How to Run FitTerm

## Requirements:
- Install Python 3.13
- Install the flask and flask-cors modules for Python using pip:
```
Windows:
pip install flask
pip install flask-cors

Mac:
pip3 install flask
pip3 install flask-cors
```

## Steps:
1. Clone this repository
2. Navigate to this repository in your terminal:
```
cd /path/to/FitTerm/
```
3. (First time setup only) Initialize the database:
```
Windows:
python ./backend/database/scripts/initialize_database.py

Mac:
python3 ./backend/database/scripts/initialize_database.py
```
4. Run the backend
```
Windows:
python ./backend/server.py

Mac:
python3 ./backend/server.py
```
5. Open the website in your file explorer or VSCode Live Server
```
Index page is located at ./frontend/index.html
```
