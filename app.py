from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from Database.config import get_connection
import pg8000.native
import os

app = Flask(__name__)
CORS(app)

# Get a database connection
conn = get_connection()

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

        result = conn.run(
            "INSERT INTO users (name, birthdate, email, password) VALUES (:name, :birthdate, :email, :password) RETURNING id",
            name=name, birthdate=birthdate, email=email, password=password
        )
        user_id = result[0][0]
        return jsonify({"message": "User registered", "user_id": user_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/events/<int:user_id>', methods=['GET'])
def get_events(user_id):
    try:
        result = conn.run("SELECT * FROM events WHERE user_id = :user_id", user_id=user_id)
        keys = ['id', 'user_id', 'title', 'event_date', 'category']
        return jsonify([dict(zip(keys, row)) for row in result])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/events', methods=['POST'])
def add_event():
    try:
        data = request.json
        result = conn.run(
            "INSERT INTO events (user_id, title, event_date, category) VALUES (:user_id, :title, :event_date, :category) RETURNING id",
            user_id=data["user_id"],
            title=data["title"],
            event_date=data["event_date"],
            category=data.get("category", "personal")
        )
        event_id = result[0][0]
        return jsonify({"message": "Event added", "event_id": event_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    try:
        data = request.json
        title = data.get("title")
        event_date = data.get("event_date")

        conn.run(
            "UPDATE events SET title = :title, event_date = :event_date WHERE id = :event_id",
            title=title, event_date=event_date, event_id=event_id
        )
        return jsonify({"message": "Event updated successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    try:
        conn.run("DELETE FROM events WHERE id = :event_id", event_id=event_id)
        return jsonify({"message": "Event deleted"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
