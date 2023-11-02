from flask import Blueprint, jsonify, request
import mysql.connector

blueprint = Blueprint('mood_api', __name__, url_prefix='/mood_api')

def connect_to_database():
    database_config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "Cps714password",
        "database": "Fitness"
    }

    try:
        db = mysql.connector.connect(**database_config)
    except Error as e:
        return jsonify({'error': str(e)})
    
    return db

@blueprint.route('/get_user_mood/<int:user_id>', methods = ['GET'])
def get_user_mood(user_id):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "SELECT * FROM Mood WHERE UserID = %s"
        cursor.execute(query, user_id)
        user_mood = cursor.fetchall()

        if not user_mood:
            return jsonify({"message": "Error, no user mood data found"}), 400
        
        return jsonify({'user_mood': user_mood})
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if db:
            db.close()
            cursor.close()

@blueprint.route('/add_user_mood', methods=['POST'])
def add_user_mood():
    try:
        user_id = request.json['user_id']
        mood_scale = request.json['mood_scale']

        db = connect_to_database()
        cursor = db.cursor()

        query = "INSERT INTO Mood (MoodScale, UserID) VALUES (%s, %s)"
        data = (mood_scale, user_id)
        cursor.execute(query, data)

        db.commit()

        return jsonify({"message": "Mood added successfully."}), 200
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if db:
            db.close()
            cursor.close()