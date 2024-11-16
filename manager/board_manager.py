import json
import os
import uuid
from datetime import datetime
from board_base import BoardBase
from utils.singletonjson import SingletonJson


class BoardManager(BoardBase):
    """
    implementation of BoardBase
    """

    def __init__(self, db_path="db/boards.json"):
        self.storage = SingletonJson(db_path)

    def create_board(self, request: str) -> str:
        data = json.loads(request)
        boards = self.storage.get_data()

        if len(data["name"]) > 64:
            raise ValueError("Board name exceeds the maximum length of 64 characters.")

        board_id = str(uuid.uuid4())
        new_board = {
            "id": board_id,
            "name": data["name"],
            "description": data.get("description", ""),
            "creation_time": datetime.utcnow().isoformat(),
            "tasks": []
        }

        boards[board_id] = new_board
        self.storage.update_data(boards)
        return json.dumps({"id": board_id})

    def list_boards(self) -> str:
        boards = self.storage.get_data()
        return json.dumps(list(boards.values()))

    def describe_board(self, request: str) -> str:
        data = json.loads(request)
        boards = self.storage.get_data()

        board = boards.get(data["id"])
        if not board:
            raise ValueError("Board not found")
        return json.dumps(board)

    def update_board(self, request: str) -> str:
        data = json.loads(request)
        boards = self.storage.get_data()

        board = boards.get(data["id"])
        if not board:
            raise ValueError("Board not found.")

        updated_board = data["board"]
        if len(updated_board["name"]) > 64:
            raise ValueError("Board name exceeds the maximum length of 64 characters")

        board.update(updated_board)
        self.storage.update_data(boards)
        return json.dumps({"status": "success"})

    def add_task(self, request: str):
        data = json.loads(request)
        boards = self.storage.get_data()

        board = boards.get(data["id"])
        if not board:
            raise ValueError("Board not found.")

        tasks = board["tasks"]
        new_task = data["task"]

        if len(new_task["title"]) > 128:
            raise ValueError("Task title exceeds the maximum length of 128 characters")
        if new_task["status"] not in ["To-Do", "In-Progress", "Done"]:
            raise ValueError("Invalid task status.")

        task_id = str(uuid.uuid4())
        new_task["id"] = task_id
        tasks.append(new_task)
        self.storage.update_data(boards)

        return json.dumps({"task_id": task_id})

    def update_task(self, request: str):
        data = json.loads(request)
        boards = self.storage.get_data()

        board = boards.get(data["board_id"])
        if not board:
            raise ValueError("Board not found.")

        tasks = board["tasks"]
        task = next((t for t in tasks if t["id"] == data["task_id"]), None)
        if not task:
            raise ValueError("Task not found.")

        updated_task = data["task"]
        if "title" in updated_task and len(updated_task["title"]) > 128:
            raise ValueError("Task title exceeds the maximum length of 128 characters")
        if "status" in updated_task and updated_task["status"] not in ["To-Do", "In-Progress", "Done"]:
            raise ValueError("Invalid task status.")

        task.update(updated_task)
        self.storage.update_data(boards)

        return json.dumps({"status": "success"})

    def delete_task(self, request: str):
        data = json.loads(request)
        boards = self.storage.get_data()

        board = boards.get(data["board_id"])
        if not board:
            raise ValueError("Board not found.")

        tasks = board["tasks"]
        board["tasks"] = [t for t in tasks if t["id"] != data["task_id"]]

        self.storage.update_data(boards)
        return json.dumps({"status": "success"})

    def list_tasks(self, request: str) -> str:
        data = json.loads(request)
        boards = self.storage.get_data()

        board = boards.get(data["id"])
        if not board:
            raise ValueError("Board not found.")

        return json.dumps(board["tasks"])
