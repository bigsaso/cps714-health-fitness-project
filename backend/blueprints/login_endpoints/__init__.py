# blueprints/login_endpoints/__init__.py
from flask import Blueprint, jsonify, request
import mysql.connector
from mysql.connector import errorcode
# to have path visible to import the connect function
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('login_api', __name__, url_prefix='/login_api')

# MySQL configuration
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Cps714password",
    "database": "Fitness"  # Change to your database name
}

@blueprint.route('/login', methods=['POST'])
def login():
    try:
        email = request.get_json().get('email')
        
        if not email:
            return jsonify({'error': 'Email is required'}), 400
        
        db, cursor = mysql_connect()
        query = "SELECT Email, Password, Salt, UserID, FirstName, LastName FROM User WHERE email = %s"
        cursor.execute(query, (email,))

        user_data = cursor.fetchone()
        cursor.close()

        if user_data:
            password = user_data[1]
            salt = user_data[2]
            userId = user_data[3]
            firstName = user_data[4]
            lastName = user_data[5]
            return jsonify({
                "message": "Login successful.",
                'email': email, 
                'password': password, 
                'salt':salt, 
                'userId':userId,
                'firstName':firstName,
                'lastName':lastName
                }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
       
@blueprint.route('/populate_database', methods=['GET'])
def populate_database():
    try:
        # Dummy data for username and password
        dummy_data = [
            ("John", "Doe", "test@testing.com", 20, 5.7, 160.0, 'password','abcdabcdabcdabcd'),
            ("Zach", "Fong", "zachf@testing.com", 24, 5.8, 150.0, 'password1','wxyzwxyzwxyzwxyz'),
            ("Tom", "Ford", "tf@testing.com", 30, 5.9, 180.0, 'password2','lmnoplmnoplmnopl')
        ]
        db,cursor = mysql_connect()

        # Insert dummy data into the User table
        for FirstName, LastName, Email, Age, Height, Weight, Password, Salt in dummy_data:
            query = "INSERT INTO User (FirstName, LastName, Email, Age, Height, Weight, Password, Salt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (FirstName, LastName, Email, Age, Height, Weight, Password, Salt))

        db.commit()

        cursor.close()

        return jsonify({'message': 'Database populated with dummy data'})

    except Exception as e:
        return jsonify({'error': str(e)})
    
@blueprint.route('/get_users', methods=['GET'])
def get_users():
    try:
        db, cursor = mysql_connect()

        # Execute a query to retrieve all users
        query = "SELECT * FROM User"
        cursor.execute(query)

        users = cursor.fetchall()

        return jsonify({'users': users})

    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        cursor.close()