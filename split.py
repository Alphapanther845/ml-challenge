import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(image_dir, output_dir, test_size=0.2, val_size=0.2):
    """Split dataset into training, validation, and test sets."""
    if not os.path.exists(image_dir):
        print(f"Error: The directory {image_dir} does not exist!")
        return
    
    all_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    train_files, test_files = train_test_split(all_files, test_size=test_size, random_state=42)
    train_files, val_files = train_test_split(train_files, test_size=val_size/(1-test_size), random_state=42)
    
    for category, files in [('train', train_files), ('val', val_files), ('test', test_files)]:
        category_dir = os.path.join(output_dir, category)
        os.makedirs(category_dir, exist_ok=True)
        for file in files:
            shutil.copy(os.path.join(image_dir, file), os.path.join(category_dir, file))

# Paths
resized_images_dir = r'C:\Users\SHAMEER.K\OneDrive\Desktop\ml challenge\student_resource 3\resizeimage'
split_dir = r'C:/Users/SHAMEER.K/OneDrive/Desktop/ml challenge/split_dataset/'

split_dataset(resized_images_dir, split_dir)
