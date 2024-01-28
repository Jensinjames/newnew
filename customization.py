```python
import json

# Shared variables
user_preferences = "resources/user_preferences.json"

# Shared function names
def update_preferences(new_preferences):
    global user_preferences
    with open(user_preferences, 'w') as f:
        json.dump(new_preferences, f)
    print("PreferencesUpdated")

# Shared data schemas
class UserPreferencesSchema:
    def __init__(self, workspace_settings, toolset_configurations):
        self.workspace_settings = workspace_settings
        self.toolset_configurations = toolset_configurations

# Function to load user preferences
def load_preferences():
    global user_preferences
    with open(user_preferences, 'r') as f:
        preferences = json.load(f)
    return UserPreferencesSchema(**preferences)

# Function to customize workspace settings
def customize_workspace(new_settings):
    preferences = load_preferences()
    preferences.workspace_settings = new_settings
    update_preferences(preferences.__dict__)

# Function to customize toolset configurations
def customize_toolset(new_configurations):
    preferences = load_preferences()
    preferences.toolset_configurations = new_configurations
    update_preferences(preferences.__dict__)
```