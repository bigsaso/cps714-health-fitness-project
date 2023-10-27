from flask import Flask, request, jsonify
from flask import Blueprint
import mysql.connector
from mysql.connector import errorcode

exercise_api = Blueprint('exercise_api', __name__)

@exercise_api.route('/add_exercise', methods=['POST'])
def add_exercise():
    try:
        repetitions = request.json['repetitions']
        numSets = request.json['numsets']
        exerciseName = request.json['exercisename']
        db = connect_to_database()

        cursor = db.cursor()
        
        query = "INSERT INTO ExerciseLog (Repetitions, NumSets, ExerciseName) VALUES (%s, %s, %s)"
        values = (repetitions, numSets, exerciseName)
        cursor.execute(query, values)
        cursor.close()
        
        return jsonify({"message": "Exercise added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@exercise_api.route('/get_exercise', methods=['GET'])
def get_exercise():
    try:
        exercise_id = request.json['exerciseid']
        db = connect_to_database()

        cursor = db.cursor()
        
        query = "SELECT * WHERE ExerciseID = %s"
        values = (exercise_id)
        cursor.execute(query, values)
        data = cursor.fetchone()
        cursor.close()

        return jsonify.dumps(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400        
        
def connect_to_database():
    data = {
        # to be changed -> read from file later or preconnect to db.
    "user": "root",
    "password": "Cps714password",
    "host": "127.0.0.1",
    "database": "Fitness"
    }
    try:
        cnx = mysql.connector.connect(**data)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    
    return cnx