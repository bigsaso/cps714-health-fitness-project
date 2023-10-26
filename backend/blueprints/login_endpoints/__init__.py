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
def check_credentials(email, password):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        query = 'SELECT * FROM User WHERE email =%s AND password =%s'
        cursor.execute(query, (email, password))

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
        query = "SELECT * FROM User"
        cursor.execute(query)

        users = cursor.fetchall()

        return jsonify({'users': users})

    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()

@blueprint.route('/login', methods=['POST'])
def login():
    email = request.args.get('Email')
    password = request.args.get('Password')

    if not email or not password:
        return jsonify({"message": "Email and password are required."}), 400

    if check_credentials(email, password):
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"message": "Login failed. Invalid credentials."}), 401
    
@blueprint.route('/populate_database', methods=['GET'])
def populate_database():
    try:
        # Dummy data for username and password
        dummy_data = [
            ("John", "Doe", "test@testing.com", 20, 5.7, 160.0, 'password'),
            ("Zach", "Fong", "zachf@testing.com", 24, 5.8, 150.0, 'password1'),
            ("Tom", "Ford", "tf@testing.com", 30, 5.9, 180.0, 'password2')
        ]
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        # Insert dummy data into the User table
        for FirstName, LastName, Email, Age, Height, Weight, Password in dummy_data:
            query = "INSERT INTO User (FirstName, LastName, Email, Age, Height, Weight, Password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (FirstName, LastName, Email, Age, Height, Weight, Password))

        db.commit()

        cursor.close()

        return jsonify({'message': 'Database populated with dummy data'})

    except Exception as e:
        return jsonify({'error': str(e)})