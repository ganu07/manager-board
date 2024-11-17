import unittest
import json
from app import app

class AssignmentAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.client = app.test_client()
        self.client.testing = True

    # User APIs
    def test_create_user_success(self):
        payload = {
            "name": "test_user",
            "display_name": "Test User"
        }
        response = self.client.post(
            '/users',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)

    def test_create_user_duplicate_name(self):
        payload = {
            "name": "test_user",
            "display_name": "Test User Duplicate"
        }
        response = self.client.post(
            '/users',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn("error", data)
        self.assertEqual(data["error"], "User name must be unique")

    def test_list_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    # Team APIs
    def test_create_team_success(self):
        payload = {
            "name": "Test Team",
            "description": "A team for testing",
            "admin": "user_001"
        }
        response = self.client.post(
            '/teams',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)

    def test_add_users_to_team_success(self):
        payload = {
            "id": "team_001",
            "users": ["user_002", "user_003"]
        }
        response = self.client.post(
            '/api/team/add-users',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Users added to team successfully")

    def test_remove_users_from_team_success(self):
        payload = {
            "id": "team_001",
            "users": ["user_002"]
        }
        response = self.client.post(
            '/api/team/remove-users',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Users removed from team successfully")

    def test_list_team_users(self):
        payload = {
            "id": "team_001"
        }
        response = self.client.post(
            '/api/team/list-users',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    # Board APIs
    def test_create_task_success(self):
        payload = {
            "board_id": "board_001",
            "title": "New Task",
            "description": "This is a test task",
            "assignee": "user_001"
        }
        response = self.client.post(
            '/api/task/create',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("task_id", data)

    def test_delete_board_success(self):
        payload = {
            "id": "board_001"
        }
        response = self.client.delete(
            '/api/board/delete',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["message"], "Board board_001 deleted successfully")

    def test_delete_board_not_found(self):
        payload = {
            "id": "non_existent_board"
        }
        response = self.client.delete(
            '/api/board/delete',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data["error"], "Board not found")

if __name__ == "__main__":
    unittest.main()
