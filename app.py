from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import pg8000.native
from Database.config import db_config

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL using pg8000
conn = pg8000.native.Connection(**db_config)

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
            "INSERT INTO users (name, birthdate, email, password) VALUES (?, ?, ?, ?) RETURNING id",
            name, birthdate, email, password
        )
        user_id = result[0][0]
        return jsonify({"message": "User registered", "user_id": user_id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/events/<int:user_id>', methods=['GET'])
def get_events(user_id):
    events = conn.run("SELECT * FROM events WHERE user_id = ?", user_id)
    keys = ['id', 'user_id', 'title', 'event_date', 'category']
    return jsonify([dict(zip(keys, row)) for row in events])

@app.route('/api/events', methods=['POST'])
def add_event():
    data = request.json
    result = conn.run(
        "INSERT INTO events (user_id, title, event_date, category) VALUES (?, ?, ?, ?) RETURNING id",
        data["user_id"], data["title"], data["event_date"], data.get("category", "personal")
    )
    event_id = result[0][0]
    return jsonify({"message": "Event added", "event_id": event_id}), 201

@app.route("/api/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.json
    title = data.get("title")
    event_date = data.get("event_date")

    conn.run(
        "UPDATE events SET title = ?, event_date = ? WHERE id = ?",
        title, event_date, event_id
    )
    return jsonify({"message": "Event updated successfully."})

@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    conn.run("DELETE FROM events WHERE id = ?", event_id)
    return jsonify({"message": "Event deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
