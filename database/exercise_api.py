from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/add_exercise', methods=['POST'])
def add_exercise(db):
    try:
        repetitions = request.json['repetitions']
        numSets = request.json['numsets']
        exerciseName = request.json['exercisename']
        
        cursor = db.cursor()
        
        query = "INSERT INTO ExerciseLog (Repetitions, NumSets, ExerciseName) VALUES (%s, %s, %s)"
        values = (repetitions, numSets, exerciseName)
        cursor.execute(query, values)
        cursor.close()
        
        return jsonify({"message": "Exercise added successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route('/get_exercise', methods=['GET'])
def get_exercise(db):
    try:
        exercise_id = request.json['exerciseid']
        
        cursor = db.cursor()
        
        query = "SELECT * WHERE ExerciseID = %s"
        values = (exercise_id)
        cursor.execute(query, values)
        data = cursor.fetchone()
        cursor.close()

        return jsonify.dumps(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400        
        

if __name__ == '__main__':
    app.run(debug=True)