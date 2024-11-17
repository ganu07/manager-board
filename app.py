import json
from flask import Flask, request, jsonify
from src.user_manager import UserManager
from src.team_manager import TeamManager
from src.board_manager import BoardManager

app = Flask(__name__)

# Initialize managers
user_manager = UserManager()
team_manager = TeamManager()
board_manager = BoardManager()

# === User APIs ===
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    try:
        response = user_manager.create_user(json.dumps(data))
        return jsonify(json.loads(response)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/users", methods=["GET"])
def list_users():
    response = user_manager.list_users()
    return jsonify(json.loads(response)), 200


@app.route("/users/<user_id>", methods=["GET"])
def describe_user(user_id):
    try:
        response = user_manager.describe_user(json.dumps({"id": user_id}))
        return jsonify(json.loads(response)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/user/get-teams', methods=['POST'])
def get_user_teams():
    data = request.get_json()
    try:
        response = user_manager.get_user_teams(data)
        return jsonify({"status": "success", "teams": response}), 200
    except ValueError as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# === Team APIs ===
@app.route("/teams", methods=["POST"])
def create_team():
    data = request.get_json()
    try:
        response = team_manager.create_team(json.dumps(data))
        return jsonify(json.loads(response)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/teams", methods=["GET"])
def list_teams():
    response = team_manager.list_teams()
    return jsonify(json.loads(response)), 200


@app.route("/teams/<team_id>", methods=["GET"])
def describe_team(team_id):
    try:
        response = team_manager.describe_team(json.dumps({"id": team_id}))
        return jsonify(json.loads(response)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


# Add Users to Team
@app.route('/api/team/add-users', methods=['POST'])
def add_users_to_team():
    data = request.get_json()
    try:
        response = team_manager.add_users_to_team(data)
        return jsonify({"status": "success", "message": response}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Remove Users from Team
@app.route('/api/team/remove-users', methods=['POST'])
def remove_users_from_team():
    data = request.get_json()
    try:
        response = team_manager.remove_users_from_team(data)
        return jsonify({"status": "success", "message": response}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# List Users in a Team
@app.route('/api/team/list-users', methods=['POST'])
def list_team_users():
    data = request.get_json()
    try:
        response = team_manager.list_team_users(data)
        return jsonify({"status": "success", "users": response}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# === Board APIs ===
@app.route("/boards", methods=["POST"])
def create_board():
    data = request.get_json()
    try:
        response = board_manager.create_board(json.dumps(data))
        return jsonify(json.loads(response)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/boards", methods=["GET"])
def list_boards():
    response = board_manager.list_boards()
    return jsonify(json.loads(response)), 200


@app.route("/boards/<board_id>", methods=["GET"])
def describe_board(board_id):
    try:
        response = board_manager.describe_board(json.dumps({"id": board_id}))
        return jsonify(json.loads(response)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@app.route("/boards/<board_id>/tasks", methods=["POST"])
def add_task(board_id):
    data = request.get_json()
    data["id"] = board_id
    try:
        response = board_manager.add_task(json.dumps(data))
        return jsonify(json.loads(response)), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/boards/<board_id>/tasks/<task_id>", methods=["PUT"])
def update_task(board_id, task_id):
    data = request.get_json()
    data.update({"board_id": board_id, "task_id": task_id})
    try:
        response = board_manager.update_task(json.dumps(data))
        return jsonify(json.loads(response)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/boards/<board_id>/tasks/<task_id>", methods=["DELETE"])
def delete_task(board_id, task_id):
    try:
        response = board_manager.delete_task(json.dumps({"board_id": board_id, "task_id": task_id}))
        return jsonify(json.loads(response)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404


@app.route("/boards/<board_id>/tasks", methods=["GET"])
def list_tasks(board_id):
    try:
        response = board_manager.list_tasks(json.dumps({"id": board_id}))
        return jsonify(json.loads(response)), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/task/create', methods=['POST'])
def create_task():
    try:
        data = request.json
        response = board_manager.create_task(json.dumps(data))
        return response, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/board/delete', methods=['DELETE'])
def delete_board():
    try:
        data = request.json
        response = board_manager.delete_board(json.dumps(data))
        return response, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400 


if __name__ == "__main__":
    app.run(debug=True)
