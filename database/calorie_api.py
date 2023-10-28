from flask import Flask, request, jsonify
from flask import Blueprint
import mysql.connector
from mysql.connector import errorcode

calorie_api = Blueprint('calorieAPI', __name__)

def connect_to_database():
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Cps714password",
        database="Fitness"
    )
    return db


@calorie_api.route('/add_calorie_intake', methods=['POST'])
def add_calorie_intake():
    try:
        user_id = request.json['user_id']
        calorie_amount = request.json['calorie_amount']
        carbohydrate = request.json['carbohydrate']
        fat = request.json['fat']
        protein = request.json['protein']
        
        db = connect_to_database()
        cursor = db.cursor()
        
        query = "INSERT INTO CalorieIntake (CalorieAmount, Carbonhydrate, Fat, Protein, UserID) VALUES (%s, %s, %s, %s, %s)"
        values = (calorie_amount, carbohydrate, fat, protein, user_id)
        cursor.execute(query, values)
        
        db.commit() # this can be removed if frontend wants to commit all data input alltogether when user is done with entering data for all trackers.
        db.close()
        
        return jsonify({"message": "Calorie intake added successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@calorie_api.route('/get_calorie_intake/<int:user_id>', methods=['GET'])
def get_calorie_intake(user_id):
    try:
        db = connect_to_database()
        cursor = db.cursor()
        
        query = "SELECT CalorieAmount, Carbonhydrate, Fat, Protein FROM CalorieIntake WHERE UserID = %s"
        cursor.execute(query, user_id)
        calorie_intake = cursor.fetchall()
        
        db.close()
        
        if not calorie_intake:
            return jsonify({"message": "No calorie intake data found."}), 404
        
        calorie_data = []
        for entry in calorie_intake:
            calorie_data.append({
                "CalorieAmount": entry[0],
                "Carbohydrate": entry[1],
                "Fat": entry[2],
                "Protein": entry[3]
            })
        
        return jsonify({"calorie data": calorie_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
