from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import mysql.connector
from Database.config import db_config

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(**db_config)
cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        name = data.get("name")
        birthdate = data.get("birthdate")
        email = data.get("email")
        password = data.get("password")

        if not all([name, birthdate, email, password]):
            return jsonify({"error": "Missing fields"}), 400

        cursor.execute(
            "INSERT INTO users (name, birthdate, email, password) VALUES (%s, %s, %s, %s)",
            (name, birthdate, email, password)
        )
        db.commit()
        user_id = cursor.lastrowid

        return jsonify({"message": "User registered", "user_id": user_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/events/<int:user_id>', methods=['GET'])
def get_events(user_id):
    cursor.execute("SELECT * FROM events WHERE user_id = %s", (user_id,))
    return jsonify(cursor.fetchall())

@app.route('/api/events', methods=['POST'])
def add_event():
    data = request.json
    cursor.execute(
        "INSERT INTO events (user_id, title, event_date, category) VALUES (%s, %s, %s, %s)",
        (data["user_id"], data["title"], data["event_date"], data.get("category", "personal"))
    )
    db.commit()
    return jsonify({"message": "Event added", "event_id": cursor.lastrowid}), 201

@app.route("/api/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.json
    title = data.get("title")
    event_date = data.get("event_date")

    cursor.execute("UPDATE events SET title = %s, event_date = %s WHERE id = %s",
                   (title, event_date, event_id))
    db.commit()
    return jsonify({"message": "Event updated successfully."})

@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
    db.commit()
    return jsonify({"message": "Event deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
