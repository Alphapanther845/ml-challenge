import os
from PIL import Image

# Directory where images are stored
image_dir = r'C:\Users\SHAMEER.K\OneDrive\Desktop\ml challenge\images'

# List all files in the directory
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Print number of images and inspect some
print(f"Number of images: {len(image_files)}")
for file in image_files[:5]:  # Inspect the first 5 images
    img_path = os.path.join(image_dir, file)
    with Image.open(img_path) as img:
        print(f"Image: {file}, Size: {img.size}, Mode: {img.mode}")
