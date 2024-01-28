```python
import json
import os
from datetime import datetime

class ProjectManager:
    def __init__(self):
        self.current_project = None
        self.current_frame = None
        self.user_preferences = self.load_preferences()

    def load_project(self, project_path):
        with open(project_path, 'r') as file:
            self.current_project = json.load(file)
        return self.current_project

    def save_project(self, project_path=None):
        if not project_path:
            project_path = f"resources/projects/{self.current_project['name']}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        with open(project_path, 'w') as file:
            json.dump(self.current_project, file)
        return project_path

    def load_preferences(self):
        if os.path.exists("resources/user_preferences.json"):
            with open("resources/user_preferences.json", 'r') as file:
                return json.load(file)
        else:
            return {}

    def update_preferences(self, new_preferences):
        self.user_preferences.update(new_preferences)
        with open("resources/user_preferences.json", 'w') as file:
            json.dump(self.user_preferences, file)
        return self.user_preferences
```