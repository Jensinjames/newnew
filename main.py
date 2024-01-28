```python
import ui_manager
import frame_editor
import image_generator
import storyboard_flow
import export_share
import project_manager
import customization

# Load user preferences
with open("resources/user_preferences.json", "r") as file:
    user_preferences = json.load(file)

# Initialize the UI Manager
ui_manager = ui_manager.UIManager(user_preferences)

# Initialize the Frame Editor
frame_editor = frame_editor.FrameEditor()

# Initialize the Image Generator
image_generator = image_generator.ImageGenerator()

# Initialize the Storyboard Flow
storyboard_flow = storyboard_flow.StoryboardFlow()

# Initialize the Export and Share module
export_share = export_share.ExportShare()

# Initialize the Project Manager
project_manager = project_manager.ProjectManager()

# Initialize the Customization module
customization = customization.Customization(user_preferences)

# Set the current project and frame to None initially
current_project = None
current_frame = None

def main():
    global current_project
    global current_frame

    # Load the UI
    ui_manager.load_ui()

    # Event loop
    while True:
        event = ui_manager.get_event()

        if event == "FrameCreated":
            current_frame = frame_editor.create_frame()
        elif event == "FrameEdited":
            frame_editor.edit_frame(current_frame)
        elif event == "ImageGenerated":
            image_generator.generate_image()
        elif event == "StoryboardReordered":
            storyboard_flow.reorder_storyboard(current_project)
        elif event == "ProjectSaved":
            project_manager.save_project(current_project)
        elif event == "ProjectLoaded":
            current_project = project_manager.load_project()
        elif event == "PreferencesUpdated":
            customization.update_preferences(user_preferences)
        elif event == "ExportStoryboard":
            export_share.export_storyboard(current_project)
        elif event == "ShareStoryboard":
            export_share.share_storyboard(current_project)

if __name__ == "__main__":
    main()
```