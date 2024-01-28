Shared Dependencies:

1. **Exported Variables**:
   - `current_project`: The current project that the user is working on.
   - `current_frame`: The current frame that the user is editing.
   - `user_preferences`: The user's personalized settings and preferences.

2. **Data Schemas**:
   - `ProjectSchema`: Defines the structure of a project, including its frames, settings, and metadata.
   - `FrameSchema`: Defines the structure of a frame, including its visual elements, composition, and metadata.
   - `UserPreferencesSchema`: Defines the structure of user preferences, including workspace settings and toolset configurations.

3. **DOM Element IDs**:
   - `editor`: The main editor area where frames are created and edited.
   - `animatic_viewer`: The viewer for previewing the storyboard's flow and transitions.
   - `image_library`: The library of imported and generated images.
   - `frame_list`: The list of frames in the current project.
   - `export_options`: The options for exporting the storyboard or frames.
   - `share_options`: The options for sharing the storyboard or frames.
   - `project_versions`: The list of saved versions of the current project.
   - `settings`: The area for adjusting project settings and user preferences.

4. **Message Names**:
   - `FrameCreated`: Emitted when a new frame is created.
   - `FrameEdited`: Emitted when a frame is edited.
   - `ImageGenerated`: Emitted when an image is generated.
   - `StoryboardReordered`: Emitted when the storyboard's sequence is reordered.
   - `ProjectSaved`: Emitted when a project is saved.
   - `ProjectLoaded`: Emitted when a project is loaded.
   - `PreferencesUpdated`: Emitted when user preferences are updated.

5. **Function Names**:
   - `create_frame()`: Creates a new frame.
   - `edit_frame()`: Edits an existing frame.
   - `generate_image()`: Generates an image based on a textual prompt.
   - `reorder_storyboard()`: Reorders the sequence of frames in the storyboard.
   - `save_project()`: Saves the current state of the project.
   - `load_project()`: Loads a saved project.
   - `update_preferences()`: Updates user preferences.
   - `export_storyboard()`: Exports the storyboard or frames.
   - `share_storyboard()`: Shares the storyboard or frames.