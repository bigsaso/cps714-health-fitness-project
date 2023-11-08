from flask import Flask, request, jsonify
from flask import Blueprint
import mysql.connector
from mysql.connector import errorcode

import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('calorie_api', __name__, url_prefix='/calorie_api')

@blueprint.route('/add_calorie_intake', methods=['POST'])
def add_calorie_intake():
    try:
        user_id = request.json['userId']
        calorie_amount = request.json['calorie_amount']
        carbohydrate = request.json['carbohydrate']
        fat = request.json['fat']
        protein = request.json['protein']
        date = request.json['date']
        
        db, cursor = mysql_connect()
        
        query = "INSERT INTO CalorieIntake (CalorieAmount, Carbonhydrate, Fat, Protein, UserID, Time) VALUES (%s, %s, %s, %s, %s)"
        values = (calorie_amount, carbohydrate, fat, protein, user_id, date)
        cursor.execute(query, values)
        cursor.close()
        db.commit() # this can be removed if frontend wants to commit all data input alltogether when user is done with entering data for all trackers.

        
        return jsonify({"message": "Calorie intake added successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@blueprint.route('/get_calorie_intake/<int:user_id>', methods=['GET'])
def get_calorie_intake(userid):
    try:       
        db, cursor = mysql_connect()
        
        query = "SELECT * FROM CalorieIntake WHERE UserID = %s"
        cursor.execute(query, userid)
        calorie_intake = cursor.fetchall()
        cursor.close()
        
        return jsonify(calorie_intake), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400  
        
        

@blueprint.route('/update_calorie_intake', methods=['PUT'])
def update_calorie_intake():
    try:
        user_id = request.json['userId']
        calorie_amount = request.json['calorie_amount']
        carbohydrate = request.json['carbohydrate']
        fat = request.json['fat']
        protein = request.json['protein']
        date = request.json['date']

        db, cursor = mysql_connect()

        query = "SELECT CalorieTrackID FROM CalorieIntake WHERE userid = %s and Time = %s"
        values = (user_id, date)
        cursor.execute(query, values)
        calorie_track_id = cursor.fetchone()[0]

        query = "UPDATE CalorieIntake SET CalorieAmount = %s, Carbonhydrate = %s, Fat = %s, Protein = %s WHERE CalorieTrackID = %s"
        values = (calorie_amount, carbohydrate, fat, protein, calorie_track_id)
        cursor.execute(query, values)
        cursor.close()
        db.commit()

        return jsonify({"message": "Exercise updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400   
