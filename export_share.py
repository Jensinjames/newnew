```python
import json
from project_manager import current_project, ProjectSchema

def export_storyboard(format='json'):
    if format == 'json':
        with open(f'resources/projects/{current_project}.json', 'w') as f:
            json.dump(ProjectSchema().dump(current_project), f)
    else:
        raise ValueError("Unsupported format")

def share_storyboard(platform='email', recipient=None):
    if platform == 'email':
        if recipient is None:
            raise ValueError("Recipient email is required for email sharing")
        # Here you would integrate with an email service to send the storyboard
        # This is a placeholder print statement
        print(f"Storyboard {current_project} has been sent to {recipient}")
    else:
        raise ValueError("Unsupported platform")
```