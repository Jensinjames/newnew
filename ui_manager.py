```python
import tkinter as tk
from tkinter import ttk
from frame_editor import create_frame, edit_frame
from image_generator import generate_image
from storyboard_flow import reorder_storyboard
from export_share import export_storyboard, share_storyboard
from project_manager import save_project, load_project
from customization import update_preferences

class UIManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Storyboard Creator")
        self.create_widgets()

    def create_widgets(self):
        self.editor = ttk.Frame(self.root)
        self.editor.grid(row=0, column=0)

        self.animatic_viewer = ttk.Frame(self.root)
        self.animatic_viewer.grid(row=0, column=1)

        self.image_library = ttk.Frame(self.root)
        self.image_library.grid(row=1, column=0)

        self.frame_list = ttk.Frame(self.root)
        self.frame_list.grid(row=1, column=1)

        self.export_options = ttk.Frame(self.root)
        self.export_options.grid(row=2, column=0)

        self.share_options = ttk.Frame(self.root)
        self.share_options.grid(row=2, column=1)

        self.project_versions = ttk.Frame(self.root)
        self.project_versions.grid(row=3, column=0)

        self.settings = ttk.Frame(self.root)
        self.settings.grid(row=3, column=1)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ui_manager = UIManager()
    ui_manager.run()
```