import os
from PIL import Image

def resize_image(img_path, output_path, size=(224, 224)):
    """Resize an image and save it to the output path."""
    with Image.open(img_path) as img:
        img = img.resize(size)
        img.save(output_path)

# Define the directories
input_dir = r'C:\Users\SHAMEER.K\OneDrive\Desktop\ml challenge\images'  # Replace with the path to your images

output_dir = r'C:\Users\SHAMEER.K\OneDrive\Desktop\ml challenge\student_resource 3\resizeimage'  # Replace with your desired output directory


# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created directory: {output_dir}")
else:
    print(f"Directory already exists: {output_dir}")

# Resize images
for file in os.listdir(input_dir):
    img_path = os.path.join(input_dir, file)
    if os.path.isfile(img_path):  # Ensure it's a file
        output_path = os.path.join(output_dir, file)
        try:
            resize_image(img_path, output_path)
            print(f"Resized and saved: {file}")
        except Exception as e:
            print(f"Error resizing {file}: {e}")
    else:
        print(f"Skipping non-file: {file}")

print("Image resizing completed.")
