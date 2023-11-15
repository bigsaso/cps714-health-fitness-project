from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('create_account_api',__name__, url_prefix='/create_account_api')

@blueprint.route('/create_account', methods=['POST'])
def create_account():
    data = request.get_json()
   
    firstName = data.get('first_name')
    lastName = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    salt = data.get('salt')
    connection, cursor = mysql_connect()

    cursor.execute("SELECT * FROM User WHERE email = %s", (email,))
    existing_user = cursor.fetchone()
   
    if existing_user:
        return jsonify({'error': 'Email already in use'}), 400

   cursor.execute("INSERT INTO User (FirstName, LastName, Email, Password, Salt) VALUES (%s, %s, %s, %s, %s)",
                   (firstName, lastName, email, password, salt))

    cursor.close()
    connection.commit()

    return jsonify({'message': 'Account created successfully'}), 201

