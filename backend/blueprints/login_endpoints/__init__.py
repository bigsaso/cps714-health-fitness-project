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
def check_credentials(email, attempt):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        query = 'SELECT * FROM User WHERE email =%s'
        cursor.execute(query, (email))

        result = cursor.fetchone()

        if result:
            password, salt = result
            return jsonify({
            "message": "OK",
            "email": "",
            "password": password,
            "salt": salt, 
            "attempted_password": attempt,}), 200
        else:
            return jsonify({
            "message": "No Email Found",
            "email": "email",
            "password": '',
            "salt": '', 
            "attempted_password": attempt,}), 400
    except Exception as e:
        print("Error:", e)
    finally:
        if db:
            db.close()

@blueprint.route('/login', methods=['POST'])
def login():
    try:
        email = request.args.get('Email')
        attempt = request.args.get('Password')

        if not email:
            return jsonify({'error': 'Email is required'}), 400
        
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT Email, Password, Salt FROM User WHERE email = %s"
        cursor.execute(query, (email,))

        user_data = cursor.fetchone()
        cursor.close()
        conn.close()

        if user_data:
            password = user_data[1]
            salt = user_data[2]
            return jsonify({
                "message": "Login successful.",'email': email, 
                'password': password, 'salt':salt, "attempt":attempt}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    #if not email or not password:
        #return jsonify({"message": "Email and password are required."}), 400

    #return check_credentials(email, password)
    #else:
        #return jsonify({"message": "Login failed. Invalid credentials."}), 401
    
@blueprint.route('/populate_database', methods=['GET'])
def populate_database():
    try:
        # Dummy data for username and password
        dummy_data = [
            ("John", "Doe", "test@testing.com", 20, 5.7, 160.0, 'password','abcdabcdabcdabcd'),
            ("Zach", "Fong", "zachf@testing.com", 24, 5.8, 150.0, 'password1','wxyzwxyzwxyzwxyz'),
            ("Tom", "Ford", "tf@testing.com", 30, 5.9, 180.0, 'password2','lmnoplmnoplmnopl')
        ]
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

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