from flask import Flask, request, jsonify

app = Flask(__name__)

# temporary database (memory storage)
users = []

# Home Route
@app.route('/')
def home():
    return "Flask User API is running!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# ADD user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added successfully"}), 201

# UPDATE user
@app.route('/users/<int:index>', methods=['PUT'])
def update_user(index):
    if index < len(users):
        users[index] = request.json
        return jsonify({"message": "User updated"})
    else:
        return jsonify({"error": "User not found"}), 404

# DELETE user
@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if index < len(users):
        users.pop(index)
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
