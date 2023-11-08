from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('steptracker_api', __name__, url_prefix='/steptracker_api')

@blueprint.route('/add_num_steps', methods=['POST'])
def add_num_steps():
    try:
        data = request.get_json()
        userId = data['userId']
        numSteps = data['numSteps']
        time = data['time']  
        connection, cursor = mysql_connect()
       
        cursor.execute("INSERT INTO StepTracker (NumSteps, UserID, Time) VALUES (%s, %s, %s)", (numSteps, userId, time))

        cursor.close()
        connection.commit()

        return jsonify({"message": "Step numbers added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

@blueprint.route('/get_num_steps/<int:userId>/<string:date>', methods=['GET'])
def get_num_steps(userId, date):
    try:
        connection, cursor = mysql_connect()
        cursor.execute("SELECT NumSteps, Time FROM StepTracker WHERE UserID = %s AND Time = %s", (userId, date))
        data = cursor.fetchall()
        cursor.close()
        
        return jsonify(data)
        
    except Exception as e:
        return jsonify({"error": str(e)})

@blueprint.route('/update_num_steps/<int:userId>/<string:date>', methods=['PUT'])
def update_num_steps(userId, date):
    try:
        data = request.get_json()
        newNumSteps = data['numSteps']
        connection, cursor = mysql_connect()
        cursor.execute("UPDATE StepTracker SET NumSteps = %s WHERE UserID = %s AND Time = %s", (newNumSteps, userId, date))
       
        cursor.close()
        connection.commit()       

        return jsonify({"message": "Step numbers have been updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})
