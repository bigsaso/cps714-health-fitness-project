from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode

blueprint=Blueprint('steptracker_api',__name__, url_prefix='/steptracker_api')

def connect_to_database():
    db = mysql.connector.connect(
        user="root",
        password="Cps714password",
        database="Fitness",
        host="127.0.0.1"
    )
    return db

@blueprint.route('/add_num_steps', methods=['POST'])
def add_num_steps():
    try:
        data = request.get_json()
        userId = data['userId']
        numSteps = data['numSteps']

        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("INSERT INTO StepTracker (NumSteps, UserID) VALUES (%s, %s)", (numSteps, userId))
        db.commit()
        cursor.close()
        db.close()

        return jsonify({"message": "Step numbers added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

    
@blueprint.route('/get_num_steps/<int:userId>', methods=['GET'])
def get_num_steps(userId):
    try:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute("SELECT NumSteps FROM StepTracker WHERE UserID = %s", (userId,))
        data = cursor.fetchall()
        cursor.close()
        db.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})


