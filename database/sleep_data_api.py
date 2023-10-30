from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode

sleep_data_api = Blueprint('sleep_data_api', __name__, url_prefix='/sleep_data_api')

def connect_to_database():
    db = mysql.connector.connect(
        user="root",
        password="Cps714password",
        database="Fitness",
        host="127.0.0.1"
    )
    return db

# Add Sleep Data
@sleep_data_api.route('/add_sleep_data', methods=['POST'])
def add_sleep_data():
    try:
        data = request.get_json()
        userId = data['userId']
        hoursSlept = data['hoursSlept']
        numDaysTracked = data['numDaysTracked']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO SleepData (HoursSlept, NumDaysTracked, UserID) VALUES (%s, %s, %s)", (hoursSlept, numDaysTracked, userId))
        mysql.connection.commit()
        cursor.close()

        return jsonify({"message": "Sleep data added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Retrieve Sleep Data
@sleep_data_api.route('/get_sleep_data/<int:userId>', methods=['GET'])
def get_sleep_data(userId):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT HoursSlept, NumDaysTracked FROM SleepData WHERE UserID = %s", (userId,))
        data = cursor.fetchall()
        cursor.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
