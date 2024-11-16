from abc import ABC, abstractmethod

class BoardBase(ABC):
    """
    Base interface for APIs to manage boards and tasks.
    Each board is associated with a specific team.
    """

    # Create a board
    @abstractmethod
    def create_board(self, request: str) -> str:
        """
        :param request: A JSON string with board details.
        {
          "name": "<board_name>",
          "description": "<board_description>",
          "team_id": "<id of the team>"
        }
        :return: A JSON string with the response {"id": "<board_id>"}

        Constraints:
            * Board name must be unique within a team.
            * Name can be max 64 characters.
            * Description can be max 128 characters.
        """
        pass

    # List all boards for a team
    @abstractmethod
    def list_boards(self, request: str) -> str:
        """
        :param request: A JSON string with team ID.
        {
          "team_id": "<id of the team>"
        }
        :return: A JSON list of boards.
        [
          {
            "id": "<board_id>",
            "name": "<board_name>",
            "description": "<board_description>",
            "creation_time": "<some date:time format>"
          }
        ]
        """
        pass

    # Create a task within a board
    @abstractmethod
    def create_task(self, request: str) -> str:
        """
        :param request: A JSON string with task details.
        {
          "board_id": "<id of the board>",
          "title": "<task_title>",
          "description": "<task_description>",
          "assignee": "<user_id>"
        }
        :return: A JSON string with the response {"id": "<task_id>"}

        Constraints:
            * Task title must be unique within a board.
            * Title can be max 64 characters.
            * Description can be max 128 characters.
        """
        pass

    # List all tasks within a board
    @abstractmethod
    def list_tasks(self, request: str) -> str:
        """
        :param request: A JSON string with board ID.
        {
          "board_id": "<id of the board>"
        }
        :return: A JSON list of tasks.
        [
          {
            "id": "<task_id>",
            "title": "<task_title>",
            "description": "<task_description>",
            "assignee": "<user_id>",
            "creation_time": "<some date:time format>"
          }
        ]
        """
        pass

    # Update a task within a board
    @abstractmethod
    def update_task(self, request: str) -> str:
        """
        :param request: A JSON string with task details to be updated.
        {
          "task_id": "<id of the task>",
          "updates": {
            "title": "<new_task_title>",
            "description": "<new_task_description>",
            "assignee": "<new_user_id>"
          }
        }
        :return: A JSON string with the response {"status": "success"}

        Constraints:
            * Task title must remain unique within a board.
            * Title can be max 64 characters.
            * Description can be max 128 characters.
        """
        pass

    # Delete a task from a board
    @abstractmethod
    def delete_task(self, request: str) -> str:
        """
        :param request: A JSON string with task ID.
        {
          "task_id": "<id of the task>"
        }
        :return: A JSON string with the response {"status": "success"}
        """
        pass

    # Delete a board
    @abstractmethod
    def delete_board(self, request: str) -> str:
        """
        :param request: A JSON string with board ID.
        {
          "board_id": "<id of the board>"
        }
        :return: A JSON string with the response {"status": "success"}
        """
        pass
