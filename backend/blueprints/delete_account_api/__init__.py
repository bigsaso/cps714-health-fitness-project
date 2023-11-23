from flask import Flask, Blueprint, request, jsonify
import mysql.connector
from mysql.connector import errorcode
import sys
sys.path.append(sys.path[0][:-len('\\backend')] + '/database')
from mysql_connection import mysql_connect

blueprint = Blueprint('delete_account_api', __name__, url_prefix='/delete_account_api')

@blueprint.route('/delete_account', methods=['DELETE'])
def delete_account():
    data = request.get_json()
    userId = data.get('userId')
    connection, cursor = mysql_connect()

    cursor.execute("SELECT * FROM User WHERE UserID = %s", (userId,))
    user = cursor.fetchone()

    if user:
        try:
            tables = ['StepTracker', 'Diet', 'Goals', 'Mood', 'CalorieIntake', 'SleepData', 'ExerciseLog']
            for table in tables:
                delete_query = f"DELETE FROM {table} WHERE UserID = %s"
                cursor.execute(delete_query, (userId,))
            
            cursor.execute("DELETE FROM User WHERE UserID = %s", (userId,))

            cursor.close()
            connection.commit()

            return jsonify({'message': f'User with UserID {userId} and their data has been deleted successfully!'})
        except Exception as e:
            connection.rollback()
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': f'User with UserID {userId} not found'})
        

