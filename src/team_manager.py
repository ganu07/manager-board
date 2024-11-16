
import json
import os
import uuid

from datetime import datetime
from base.team_base import TeamBase
from utils.singletonjson import SingletonJson


class TeamManager(TeamBase):
    """
    Implementation of Teambase
    """
    
    def __init__(self, db_path="db/teams.json"):
        self.storage = SingletonJson(db_path)


    def create_team(self, request):
        data = json.loads(request)
        teams = self.storage.get_data()
        
        if len(data["name"]) > 64:
            raise ValueError("Team name exceed with maximum 64 character")
        if len(data.get("description", "")) > 128:
            raise ValueError("Description exceeds with maximum length 128")
        if any(team["name"] == data["name"] for team in teams.values()):
            raise ValueError("team name must be unique")
        
        team_id = str(uuid.uuid4())
        new_team = {
            "id": team_id,
            "name" : data["name"],
            "description": data.get("description", ""),
            "creation_time": datetime.utcnow().isoformat(),
            "admin": data["admin"],
            "users": []
        }
        teams[team_id] = new_team
        self.storage.update_data(teams)
        return json.dumps({"id": team_id})
    
    def list_teams(self):
        teams = self.storage.get_data()
        return json.dumps(list(teams.values()))
    
    def describe_team(self, request: str) -> str:
        data = json.loads(request)
        teams = self.storage.get_data()
        
        team = teams.get(data["id"])
        if not team:
            raise ValueError("Team not found")
        return json.dumps(team)
    
    def update_team(self, request):
        data = json.loads(request)
        teams = self.storage.get_data()
        
        team = teams.get(data["id"])
        if not team:
            raise ValueError("team not found")
        
        updated_team = data["team"]
        if len(updated_team["name"]) > 64:
            raise ValueError("Team name should not be greater than 64 character")
        if len(updated_team.get("description", "")) > 128:
            raise ValueError("description should not be greater than 128 characters")
        
        team.update(updated_team)
        self.storage.update_data(teams)
        return json.dumps({'status': "success"})
    
    def add_users_to_team(self, request: str):
        data = json.loads(request)
        teams = self.storage.get_data()
        
        team = teams.get(data["id"])
        if not team:
            raise ValueError("team not found")
        if len(data["users"]) + len(team["users"]) > 50:
            raise ValueError("can not exceed 50 users in a team")
        
        team["users"].extend(data["users"])
        team["users"] = list(set(team["users"]))
        self.storage.update_data(teams)
        
    def remove_users_from_team(self, request):
        data = json.loads(request)
        teams = self.storage.get_data()
        
        team = teams.get(data["id"])
        if not team:
            raise ValueError("Team not found")
        
        team["users"] = [user for user in team["users"] if user not in data["users"]]
        self.storage.update_data(teams)
        
    def list_team_users(self, request: str):
        data = json.loads(request)
        teams = self.storage.get_data()
        
        team = teams.get(data["id"])
        if not team:
            raise ValueError("Team not found")
        
        return json.dumps(team["users"])
