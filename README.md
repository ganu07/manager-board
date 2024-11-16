# Team Project Planner API

This project implements a Team Project Planner tool using Python. The tool consists of APIs for:
- Managing users
- Managing teams
- Managing a team board and tasks within the board

The project follows a modular structure with base abstract classes for each functionality and concrete implementations. 

## Project Overview

### Features:
- **User Management**: Allows the creation, listing, updating, and deletion of users.
- **Team Management**: Allows teams to be created, updated, users to be added/removed, and team information to be retrieved.
- **Board Management**: Provides functionality for creating boards, adding tasks, updating tasks, and deleting boards.

### Design:
- The application uses **Singleton Pattern** for managing data persistence using JSON files.
- Each module has abstract base classes defining the API methods, and concrete implementations handle the actual logic.
- **Persistence**: Data is stored in local JSON files (`db/` folder) for simplicity and scalability.

---

## How to Run the Application

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/team-project-planner.git
    cd team-project-planner
    ```

2. **Install Dependencies**:
    If you're using `pip`, create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate    # For macOS/Linux
    venv\Scripts\activate       # For Windows
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    You can interact with the application via the script `app.py`, which manages the entire flow. It interacts with `UserManager`, `TeamManager`, and `BoardManager` for their respective operations.

    ```bash
    python app.py
    ```

---

## API Endpoints and Usage

The following methods are implemented:

### User Management
- **Create a User**:
    ```python
    create_user({"name": "john_doe", "display_name": "John Doe"})
    ```

- **List Users**:
    ```python
    list_users()
    ```

- **Describe a User**:
    ```python
    describe_user({"id": "user_001"})
    ```

- **Update User**:
    ```python
    update_user({"id": "user_001", "user": {"display_name": "John Updated"}})
    ```

- **Get User Teams**:
    ```python
    get_user_teams({"id": "user_001"})
    ```

### Team Management
- **Create a Team**:
    ```python
    create_team({"name": "project_alpha", "description": "Team for Project Alpha", "admin": "user_001"})
    ```

- **List Teams**:
    ```python
    list_teams()
    ```

- **Describe a Team**:
    ```python
    describe_team({"id": "team_001"})
    ```

- **Update Team**:
    ```python
    update_team({"id": "team_001", "team": {"name": "updated_team", "description": "Updated Team Description", "admin": "user_002"}})
    ```

- **Add Users to Team**:
    ```python
    add_users_to_team({"id": "team_001", "users": ["user_002", "user_003"]})
    ```

- **Remove Users from Team**:
    ```python
    remove_users_from_team({"id": "team_001", "users": ["user_002"]})
    ```

- **List Users in a Team**:
    ```python
    list_team_users({"id": "team_001"})
    ```

### Board Management
- **Create a Board**:
    ```python
    create_board({"name": "project_board", "team_id": "team_001"})
    ```

- **Describe a Board**:
    ```python
    describe_board({"id": "board_001"})
    ```

- **Update a Board**:
    ```python
    update_board({"id": "board_001", "board": {"name": "Updated Board", "team_id": "team_002"}})
    ```

- **Delete a Board**:
    ```python
    delete_board({"id": "board_001"})
    ```

- **Create a Task on a Board**:
    ```python
    create_task({"board_id": "board_001", "title": "New Task", "description": "Task description", "assignee": "user_001"})
    ```

- **List Tasks in a Board**:
    ```python
    list_board_tasks({"id": "board_001"})
    ```

- **Update a Task**:
    ```python
    update_task({"board_id": "board_001", "task_id": "task_001", "status": "completed"})
    ```

- **Delete a Task**:
    ```python
    delete_task({"board_id": "board_001", "task_id": "task_001"})
    ```

---

## Example JSON Data

### Sample User JSON:
```json
{
    "name": "john_doe",
    "display_name": "John Doe"
}
```

### Sample Team JSON:
```json
{
    "name": "project_alpha",
    "description": "Team for Project Alpha",
    "admin": "user_001"
}
```

### Sample Board JSON:
```json
{
    "name": "project_board",
    "team_id": "team_001"
}
```

### Sample Task JSON:
```json
{
    "title": "New Task",
    "description": "Task description",
    "assignee": "user_001",
    "board_id": "board_001"
}
```

## Project File Structure
├── db/
│   ├── users.json         # Persistent storage for user data
│   ├── teams.json         # Persistent storage for team data
│   ├── boards.json        # Persistent storage for board data
├── base/
│   ├── user_base.py       # Abstract base class for user management
│   ├── team_base.py       # Abstract base class for team management
│   ├── board_base.py      # Abstract base class for board management
├── src/
│   ├── user_manager.py    # Implementation of user management
│   ├── team_manager.py    # Implementation of team management
│   ├── board_impl.py      # Implementation of board and task management
├── utils/
│   ├── singleton_json.py  # Singleton JSON file for managing input/output data
├── requirements.txt       # Required Python libraries
├── README.md              # Documentation
├── app.py                 # Entry point for running the APIs

