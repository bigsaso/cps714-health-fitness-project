from flask import Flask, request, jsonify
from flask import Blueprint
import mysql.connector
from mysql.connector import errorcode
# to have path visible to import the connect function
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

exercise_api = Blueprint('exercise_api', __name__)

@exercise_api.route('/add_exercise', methods=['POST'])
def add_exercise():
    try:
        repetitions = request.json['repetitions']
        numSets = request.json['numsets']
        exerciseName = request.json['exercisename']

        db, cursor = mysql_connect()
                
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
        db, cursor = mysql_connect()
        
        query = "SELECT * WHERE ExerciseID = %s"
        values = (exercise_id)
        cursor.execute(query, values)
        data = cursor.fetchone()
        cursor.close()

        return jsonify.dumps(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400        
        