from flask import Flask, request, jsonify
from status_codes import *
from database_connection import DatabaseConnection

connection_string = "FitTerm.db"
app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    Expects 'username' and 'password' in the request JSON body.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    conn = DatabaseConnection(connection_string)
    conn.user_table.add_user(username, password)
    conn.close()
    
    return jsonify({'message': 'User created successfully'}), HTTP_CREATED

@app.route('/verify_user', methods=['GET'])
def verify_user():
    """
    Endpoint to verify a user exists and has entered the correct password.
    Expects 'username' and 'password' in the request JSON body.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = DatabaseConnection(connection_string)
    user = conn.user_table.get_user(username)
    conn.close()

    if user == None:
        return jsonify({'message': 'User not found'}), HTTP_NOT_FOUND
    
    elif password != user.password:
        return jsonify({'message': 'User found, incorrect password'}), HTTP_UNAUTHORIZED
    
    else:
        return jsonify({'message': 'User found, correct password'}), HTTP_OK

if __name__ == "__main__":
    app.run(debug=True, port=8080)