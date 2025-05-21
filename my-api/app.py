from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'MyNotes'
CORS(app, supports_credentials=True)

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SQLfcalista09*"
    )
    
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS my_notes;")
    cursor.close()
    conn.close()

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SQLfcalista09*",
        database="my_notes"
    )

db = get_db_connection()
cursor = db.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        description TEXT,
        day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
        category ENUM('Important', 'Urgent', 'Regular') NOT NULL DEFAULT 'Regular',
        status ENUM('Active', 'Deleted', 'Done') NOT NULL DEFAULT 'Active',
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
""")
db.commit()
cursor.close()
db.close()

HARDCODED_USERNAME = 'admin'
HARDCODED_PASSWORD = 'abcdef'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid login"}), 401


@app.route("/taskMonitoring", methods=["GET"])
def taskMonitoring():
    return jsonify({"message": "Welcome to Task Monitoritng Page"}), 200


@app.route("/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Logged out"}), 200


@app.route("/api/tasks", methods=["GET"])
def get_tasks():

    day = request.args.get('day')
    category = request.args.get('category')
    status = request.args.get('status', 'Active')

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT id, title, description, day, category, status, CONVERT_TZ(last_updated, 'UTC', 'Asia/Jakarta') AS last_updated FROM tasks WHERE status != 'Deleted'"
    params = []
    
    if day:
        query += " AND day = %s"
        params.append(day)
    
    if category:
        query += " AND category = %s"
        params.append(category)
    
    if status:
        query += " AND status = %s"
        params.append(status)
    
    cursor.execute(query, params)
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def add_task():

    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")
    day = data.get("day")
    category = data.get("category", "Regular")

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        """INSERT INTO tasks 
        (title, description, day, category, status, last_updated) 
        VALUES (%s, %s, %s, %s, 'Active', %s)""",
        (title, description, day, category, datetime.now())
    )
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Task added successfully"}), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    day = data.get("day")
    category = data.get("category")
    status = data.get("status")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        """UPDATE tasks SET 
        title=%s, description=%s, day=%s, category=%s, status=%s, last_updated=%s 
        WHERE id=%s""",
        (title, description, day, category, status, datetime.now(), task_id)
    )
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Task updated successfully"}), 200


@app.route("/api/tasks/<int:task_id>", methods=["PATCH"])
def markAsDone(task_id):
    
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "UPDATE tasks SET status='Done', last_updated=%s WHERE id=%s",
        (datetime.now(), task_id)
    )

    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Task updated successfully"}), 200


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "UPDATE tasks SET status='Deleted', last_updated=%s WHERE id=%s",
        (datetime.now(), task_id)
    )
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)