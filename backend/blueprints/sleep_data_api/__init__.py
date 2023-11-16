from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('sleep_data_api', __name__, url_prefix='/sleep_data_api')

# Add Sleep Data
@blueprint.route('/add_sleep_data', methods=['POST'])
def add_sleep_data():
    try:
        data = request.get_json()
        userId = data['userId']
        hoursSlept = data['hoursSlept']
        date = data['date']

        connection, cursor = mysql_connect()

        cursor.execute("INSERT INTO SleepData (HoursSlept, UserID, Time) VALUES (%s, %s, %s)", (hoursSlept, userId, date))
        cursor.close()
        connection.commit()

        return jsonify({"message": "Sleep data added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Retrieve Sleep Data
@blueprint.route('/get_sleep_data/<int:userId>', methods=['GET'])
def get_sleep_data(userId):
    try:
        connection, cursor = mysql_connect()

        cursor.execute("SELECT * FROM SleepData WHERE UserID = %s", (userId,))
        data = cursor.fetchall()
        cursor.close()
        
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
    
# Retrieve Sleep Hours For The Past Week
@blueprint.route('/get_sleep_hours/<int:userId>', methods=['GET'])
def get_sleep_hours(userId):
    try:
        connection, cursor = mysql_connect()

        cursor.execute("SELECT HoursSlept FROM SleepData WHERE UserID = %s ORDER BY Time DESC LIMIT 7", (userId,))
        data = cursor.fetchall()
        cursor.close()
        
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# Update Sleep Data
@blueprint.route('/update_sleep_data', methods=['PUT'])
def update_sleep_data():
    try:
        data = request.get_json()
        userId = data['userId']
        hoursSlept = data['hoursSlept']
        numDaysTracked = data['numDaysTracked']
        date = data['date']

        connection, cursor = mysql_connect()

        cursor.execute("UPDATE SleepData SET HoursSlept = %s, NumDaysTracked = %s, Time = %s WHERE UserID = %s", (hoursSlept, numDaysTracked, date, userId))
        result = cursor.fetchall()
        cursor.close()
        connection.commit()

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# Update Sleep Data by Date
@blueprint.route('/update_sleep_data_by_date', methods=['PUT'])
def update_sleep_data_by_date():
    try:
        data = request.get_json()
        userId = data['userId']
        hoursSlept = data['hoursSlept']
        numDaysTracked = data['numDaysTracked']
        date = data['date']

        connection, cursor = mysql_connect()

        cursor.execute("UPDATE SleepData SET HoursSlept = %s, NumDaysTracked = %s WHERE UserID = %s AND Time = %s", (hoursSlept, numDaysTracked, userId, date))
        result = cursor.fetchall()
        cursor.close()
        connection.commit()

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

# Delete Sleep Data by ID
@blueprint.route('/delete_sleep_data/<int:userId>', methods=['DELETE'])
def delete_sleep_data(userId):
    try:
        connection, cursor = mysql_connect()

        cursor.execute("DELETE FROM SleepData WHERE UserID = %s", (userId,))
        result = cursor.fetchall()
        cursor.close()
        connection.commit()

        return jsonify({"message": "Sleep data deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Delete Sleep Data by Date
@blueprint.route('/delete_sleep_data_by_date', methods=['DELETE'])
def delete_sleep_data_by_date():
    try:
        data = request.get_json()
        userId = data['userId']
        date = data['date']

        connection, cursor = mysql_connect()

        cursor.execute("DELETE FROM SleepData WHERE UserID = %s AND Time = %s", (userId, date))
        result = cursor.fetchall()
        cursor.close()
        connection.commit()

        return jsonify({"message": "Sleep data deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})
    
