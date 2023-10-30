from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode

step_tracker_api = Blueprint('step_tracker_api', __name__, url_prefix='/step_tracker_api')

def connect_to_database():
    db = mysql.connector.connect(
        user="root",
        password="Cps714password",
        database="Fitness",
        host="127.0.0.1"
    )
    return db

# Add Sleep Data
@step_tracker_api.route('/add_steps', methods=['POST'])
def add_steps():
    try:
        data = request.get_json()
        userId = data['userId']
        numSteps = data['NumSteps']
        

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO StepTracker (NumSteps, UserID) VALUES (%s, %s, %s)", (numSteps, userId))
        mysql.connection.commit()
        cursor.close()

        return jsonify({"message": "Number of steps added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

# Retrieve Sleep Data
@step_tracker_api.route('/add_steps/<int:userId>', methods=['GET'])
def get_sleep_data(userId):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT NumSteps FROM StepTracker WHERE UserID = %s", (userId,))
        data = cursor.fetchall()
        cursor.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})