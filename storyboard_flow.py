```python
import json
from project_manager import current_project, ProjectSchema

def reorder_storyboard(new_order):
    """
    Reorders the sequence of frames in the storyboard based on the new order provided.
    """
    current_project.frames = [current_project.frames[i] for i in new_order]
    return current_project

def apply_transition(frame_id, transition):
    """
    Applies a transition effect to a frame.
    """
    current_frame = current_project.frames[frame_id]
    current_frame.transition = transition
    return current_frame

def save_storyboard_flow():
    """
    Saves the current storyboard flow to the project.
    """
    with open(f'resources/projects/{current_project.id}.json', 'w') as f:
        json.dump(current_project, f, cls=ProjectSchema)

def load_storyboard_flow(project_id):
    """
    Loads a storyboard flow from a saved project.
    """
    with open(f'resources/projects/{project_id}.json', 'r') as f:
        current_project = json.load(f, cls=ProjectSchema)
    return current_project
```