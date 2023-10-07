# blueprints/login_endpoints/__init__.py
from flask import Blueprint, jsonify, request
import mysql.connector

blueprint = Blueprint('login_api', __name__, url_prefix='/login_api')

# MySQL configuration
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Cps714password",
    "database": "Fitness"  # Change to your database name
}


# Function to check user credentials
def check_credentials(username, password):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        query = 'SELECT * FROM users WHERE username =%s AND password =%s'
        cursor.execute(query, (username, password))

        result = cursor.fetchone()

        if result:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        if db:
            db.close()

@blueprint.route('/get_users', methods=['GET'])
def get_users():
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor(dictionary=True)

        # Execute a query to retrieve all users
        query = "SELECT * FROM users"
        cursor.execute(query)

        users = cursor.fetchall()

        return jsonify({'users': users})

    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()

@blueprint.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    if check_credentials(username, password):
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"message": "Login failed. Invalid credentials."}), 401
    
@blueprint.route('/populate_database', methods=['GET'])
def populate_database():
    try:
        # Dummy data for username and password
        dummy_data = [
            ("user1", "password1"),
            ("user2", "password2"),
            ("user3", "password3"),
        ]
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Insert dummy data into the users table
        for username, password in dummy_data:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))

        db.commit()

        cursor.close()

        return jsonify({'message': 'Database populated with dummy data'})

    except Exception as e:
        return jsonify({'error': str(e)})