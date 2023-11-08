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
        repetitions = request.json['reps']
        numSets = request.json['sets']
        exerciseName = request.json['name']
        userid = request.json['inputId']
        date = request.json['date']

        db, cursor = mysql_connect()
                
        query = "INSERT INTO ExerciseLog (Repetitions, NumSets, ExerciseName, UserID, Time) VALUES (%s, %s, %s, %s, %s)"
        values = (repetitions, numSets, exerciseName, userid, date)
        #query = "INSERT INTO ExerciseLog (Repetitions, NumSets, ExerciseName, UserID) VALUES (%s, %s, %s, %s)"
        #values = (repetitions, numSets, exerciseName, userid)
        cursor.execute(query, values)
        cursor.close()
        db.commit()
        
        return jsonify({"message": "Exercise added successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@exercise_api.route('/get_exercise/<int:userid>', methods=['GET'])
def get_exercise(userid):
    try:
        db, cursor = mysql_connect()
        
        query = "SELECT * FROM exerciselog WHERE UserID = %s"
        values = (userid,)
        cursor.execute(query, values)
        data = cursor.fetchall()
        cursor.close()

        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400        
        

@exercise_api.route('/update_exercise', methods=['PUT'])
def upt_exercise():
    try:
        repetitions = request.json['reps']
        numSets = request.json['sets']
        exerciseName = request.json['name']
        userid = request.json['inputId']
        date = request.json['date']

        db, cursor = mysql_connect()

        query = "SELECT exerciseid FROM exerciselog WHERE userid = %s and exerciseName = %s"
        values = (userid, exerciseName)
        cursor.execute(query, values)
        exercise_id = cursor.fetchone()[0]

        query = "UPDATE exerciselog SET Repetitions = %s, NumSets = %s, ExerciseName = %s WHERE exerciseid = %s"
        values = (repetitions, numSets, exerciseName, exercise_id)
        cursor.execute(query, values)
        cursor.close()
        db.commit()

        return jsonify({"message": "Exercise updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400        
