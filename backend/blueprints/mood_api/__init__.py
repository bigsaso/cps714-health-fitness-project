from flask import Flask, request, jsonify
from flask import Blueprint
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('mood_api', __name__, url_prefix='/mood_api')

@blueprint.route('/get_user_mood/<int:user_id>', methods=['GET'])
def get_user_mood(user_id):
    try:
        db = mysql_connect()
        cursor = mysql_connect()

        query = "SELECT * FROM Mood WHERE UserID = %s"
        cursor.execute(query, user_id)
        user_mood = cursor.fetchall()
        cursor.close()
        db.close()

        if not user_mood:
            return jsonify({"message": "Error, no user mood data found"}), 404
        
        return jsonify({'user_mood': user_mood}), 200
    except Exception as e:
        return jsonify({'error': str(e)})

@blueprint.route('/add_user_mood', methods=['POST'])
def add_user_mood():
    try:
        user_id = request.json['user_id']
        mood_scale = request.json['mood_scale']
        dateandtime = request.json['dateandtime']

        db = mysql_connect()
        cursor = mysql_connect()
        cursor = db.cursor()

        query = "INSERT INTO Mood (MoodScale, UserID, Time) VALUES (%s, %s, %s)"
        data = (mood_scale, user_id, dateandtime)
        cursor.execute(query, data)

        db.commit()
        cursor.close()
        db.close()

        return jsonify({"message": "Mood added successfully."}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)})
    
@blueprint.route('/update_user_mood', methods=['POST'])
def update_user_mood():
    try:
        user_id = request.json['user_id']
        mood_scale = request.json['mood_scale']
        dateandtime = request.json['dateandtime']

        db = mysql_connect()
        cursor = mysql_connect()
        cursor = db.cursor()
        
        query = "SELECT UserID FROM Mood WHERE UserID = %s"
        data = (user_id)
        cursor.execute(query, data)
        user_id = cursor.fetchone()[0]
        
        query = "UPDATE Mood SET MoodScale = %s, Time = %s WHERE UserID = %s"
        data = (mood_scale, dateandtime, user_id)
        cursor.execute(query, data)
        
        db.commit()
        cursor.close()
        db.close()
        
        return jsonify({"message": "Mood updated successfully."}), 200

    except Exception as e:
        return jsonify({'error': str(e)})