```python
import os
from ai_image_generator import AIImageGenerator

# Shared variables
current_project = None
current_frame = None

# Message names
ImageGenerated = "ImageGenerated"

class ImageGenerator:
    def __init__(self):
        self.generator = AIImageGenerator()

    def generate_image(self, text_prompt, negative_prompts=[]):
        # Generate image using AI
        image_path = self.generator.generate(text_prompt, negative_prompts)

        # Update current frame with new image
        current_frame.add_image(image_path)

        # Emit ImageGenerated message
        self.emit(ImageGenerated, image_path)

    def emit(self, message, data):
        # This function will emit a message to the rest of the application
        # The implementation of this function depends on the specific architecture of the application
        pass

    def refine_image(self, image_path, negative_prompts):
        # Refine image using AI
        refined_image_path = self.generator.refine(image_path, negative_prompts)

        # Replace old image with refined image in current frame
        current_frame.replace_image(image_path, refined_image_path)

        # Emit ImageGenerated message
        self.emit(ImageGenerated, refined_image_path)
```