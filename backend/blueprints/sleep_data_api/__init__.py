from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode

blueprint = Blueprint('sleep_data_api', __name__, url_prefix='/sleep_data_api')

def connect_to_database():
    db = mysql.connector.connect(
        user="root",
        password="Cps714password",
        database="Fitness",
        host="127.0.0.1"
    )
    return db

# Add Sleep Data
@blueprint.route('/add_sleep_data', methods=['POST'])
def add_sleep_data():
    try:
        data = request.get_json()
        userId = data['userId']
        hoursSlept = data['hoursSlept']
        numDaysTracked = data['numDaysTracked']

        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("INSERT INTO SleepData (HoursSlept, NumDaysTracked, UserID) VALUES (%s, %s, %s)", (hoursSlept, numDaysTracked, userId))
        db.commit()
        cursor.close()  

        return jsonify({"message": "Sleep data added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Retrieve Sleep Data
@blueprint.route('/get_sleep_data/<int:userId>', methods=['GET'])
def get_sleep_data(userId):
    try:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("SELECT HoursSlept, NumDaysTracked FROM SleepData WHERE UserID = %s", (userId,))
        data = cursor.fetchall()
        cursor.close()
        db.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})
