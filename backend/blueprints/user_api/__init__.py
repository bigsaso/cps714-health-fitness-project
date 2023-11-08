from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('user_api', __name__, url_prefix='/user_api')

@blueprint.route('/get_user_data/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    try:
        db, cursor = mysql_connect()

        query = "SELECT Age, Height, Weight FROM User WHERE UserID = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchall()
        cursor.close()

        return jsonify({'user_data': user_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)})

#Talk about in sprint 4, api should not be adding since that is account creation job(Only should get and update)
@blueprint.route('/add_user_data', methods=['POST'])
def add_user_data():
    try:
        user_age = request.json['user_age']
        user_height = request.json['user_height']
        user_weight = request.json['user_weight']

        db, cursor = mysql_connect()

        query = "INSERT INTO User (Age, Height, Weight) VALUES (%s, %s, %s)"
        data = (user_age, user_height, user_weight)
        cursor.execute(query, data)

        cursor.close()
        db.commit()

        return jsonify({"message": "User data added successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)})

@blueprint.route('/update_user_data', methods=['PUT'])
def update_user_data():
    try:
        user_id = request.json['user_id']
        user_age = request.json['user_age']
        user_height = request.json['user_height']
        user_weight = request.json['user_weight']

        db, cursor = mysql_connect()

        query = "UPDATE User SET Age = %s, Height = %s, Weight = %s WHERE UserID = %s"
        data = (user_age, user_height, user_weight, user_id)
        cursor.execute(query, data)

        cursor.close()
        db.commit()

        return jsonify({"message": "User data updated successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)})