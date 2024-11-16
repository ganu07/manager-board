import json
import os
import uuid
from datetime import datetime
from base.user_base import UserBase
from utils.singletonjson import SingletonJson


class UserManager(UserBase):
    """
    implmentation of user manager
    """
    
    def __init__(self, db_path="db/users.json"):
        self.storage = SingletonJson(db_path)
    
    def create_user(self, request: str) -> str:
        data = json.loads(request)
        users = self.storage.get_data()
        
        if len(data["names"]) > 64 or len(data["display_name"]) > 64:
            raise ValueError("name or display name should not be greater than 64 characters")
        if any(user["name"] == data["name"] for user in users.values()):
            raise ValueError("user name must be unique")
        
        user_id = str(uuid.uuid4())
        new_user = {
            "id": user_id,
            "name": data["name"],
            "display_name": data["display_name"],
            "creation_time": datetime.utcnow().isoformat()
        }
        users[user_id] = new_user
        self.storage.update_data(users)
        return json.dumps({"id": user_id})
    
    def list_users(self) -> str:
        users = self.storage.get_data()
        return json.dumps(list(users.values()))
    
    def describe_user(self, request: str) -> str:
        data = json.loads(request)
        users = self.storage.get_data()
        user = users.get(data["id"])
        if not user:
            raise ValueError("User not found.")
        return json.dumps(user)
    
    def update_user(self, request: str) -> str:
        data = json.loads(request)
        users = self.storage.get_data()
        user = users.get(data["id"])
        if not user:
            raise ValueError("User not found.")
        updated_user = data["user"]
        updated_user = data["user"]
        if "name" in updated_user:
            raise ValueError("User name cannot be updated")
        if "display_name" in updated_user and len(updated_user["display_name"]) > 64:
            raise ValueError("Display name exceeds the maximum length of 64 characters")

        user.update(updated_user)
        self.storage.update_data(users)
        return json.dumps({"status": "success"})
        
    def get_user_teams(self, request: str) -> str:
        pass