```python
from resources.frames import FrameSchema
from resources.projects import ProjectSchema

current_frame = None
current_project = None

def create_frame():
    global current_frame
    current_frame = FrameSchema()
    current_project.frames.append(current_frame)
    return current_frame

def edit_frame(frame_id, composition=None, background=None, foreground=None, static_dynamic=None):
    frame = next((f for f in current_project.frames if f.id == frame_id), None)
    if frame:
        if composition:
            frame.composition = composition
        if background:
            frame.background = background
        if foreground:
            frame.foreground = foreground
        if static_dynamic is not None:
            frame.static_dynamic = static_dynamic
        return frame
    else:
        raise ValueError(f"No frame found with id {frame_id}")

def delete_frame(frame_id):
    frame = next((f for f in current_project.frames if f.id == frame_id), None)
    if frame:
        current_project.frames.remove(frame)
    else:
        raise ValueError(f"No frame found with id {frame_id}")
```