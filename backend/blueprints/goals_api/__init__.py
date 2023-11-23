from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('goals_api', __name__, url_prefix='/goals_api')

@blueprint.route('/get_user_goals/<int:user_id>', methods=['GET'])
def get_user_goals(user_id):
    try:
        db, cursor = mysql_connect()

        query = "SELECT * FROM Goals WHERE UserID = %s"
        cursor.execute(query, (user_id,))
        user_goal = cursor.fetchall()
        cursor.close()

        
        return jsonify({'user_goals':user_goal}),200
    except Exception as e:
        return jsonify({'error': str(e)})

@blueprint.route('/add_user_goals', methods=['POST'])
def add_user_goals():
    try:
        user_id = request.json['user_id']
        weight_goal = request.json['weight_goal']
        daily_calorie_burn = request.json['daily_calorie_burn']
        date = request.json['date']

        db, cursor = mysql_connect()

        query = "INSERT INTO Goals (WeightGoal, DailyCalorieBurn, UserID, Time) VALUES (%s, %s, %s, %s)"
        data = (weight_goal, daily_calorie_burn, user_id, date)
        cursor.execute(query, data)

        cursor.close()
        db.commit()

        return jsonify({"message": "Goals added successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)})

@blueprint.route('/update_user_goals', methods=['PUT'])
def update_user_goals():
    try:
        user_id = request.json['user_id']
        weight_goal = request.json['weight_goal']
        daily_calorie_burn = request.json['daily_calorie_burn']
        date = request.json['date']

        db, cursor = mysql_connect()

        query = "UPDATE Goals SET WeightGoal = %s, DailyCalorieBurn = %s, Time = %s WHERE UserID = %s"
        data = (weight_goal, daily_calorie_burn, date, user_id)
        cursor.execute(query, data)

        cursor.close()
        db.commit()

        return jsonify({"message": "Goals updated successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)})