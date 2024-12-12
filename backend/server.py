from flask import Flask, request, jsonify
from flask_cors import CORS
from status_codes import *
from database_connection import DatabaseConnection

connection_string = "FitTerm.db"
app = Flask(__name__)
CORS(app)

@app.route('/create-user', methods=['POST'])
def create_user():
    """
    Endpoint to create a new user.
    Expects 'username' and 'password' in the request JSON body.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    created = False
    
    conn = DatabaseConnection(connection_string)
    user = conn.user_table.get_user(username)
    if user == None:
        conn.user_table.add_user(username, password)
        created = True
    conn.close()
    
    if created:
        return jsonify({'message': 'User created successfully'}), HTTP_CREATED
    
    else:
        return jsonify({'message': 'User with that username already exists'}), HTTP_CONFLICT

@app.route('/verify-user', methods=['POST'])
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
        return jsonify({
            'message': 'User found, incorrect password',
            'username': username
        }), HTTP_UNAUTHORIZED
    
    else:
        return jsonify({
            'message': 'User found, correct password',
            'username': username
        }), HTTP_OK

@app.route('/add-activity', methods=['POST'])
def add_activity():
    """
    Endpoint to add a new activity.
    Expects 'associated_user', 'name', 'description', 'timestamp', and 'completion' in the request JSON body.
    """
    data = request.get_json()

    associated_user = data.get('associated_user')
    name = data.get('name')
    description = data.get('description')
    timestamp = data.get('timestamp')
    completion = data.get('completion')

    conn = DatabaseConnection(connection_string)
    conn.activity_table.add_activity(associated_user, name, description, timestamp, completion)
    conn.close()

    return jsonify({
        'message': 'Activity added to log',
    }), HTTP_OK

@app.route('/get-activities', methods=['GET'])
def get_activities():
    """
    Endpoint to retrieve activities for a user.
    Expects 'username' in the request JSON body.
    """

    username = request.args.get('username')

    conn = DatabaseConnection(connection_string)
    activities = conn.activity_table.get_activities(username)
    conn.close()

    activities_json = []
    for activity in activities:
        activity_dict = {
            'associated_user': activity.associated_user,
            'id': activity.id,
            'name': activity.name,
            'description': activity.description, 
            'timestamp': activity.timestamp,
            'completion': activity.completion
        }
        activities_json.append(activity_dict)

    return jsonify({'activities': activities_json}), 200

if __name__ == "__main__":
    app.run(debug=True, port=8080)