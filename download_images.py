import pandas as pd
import os
import requests
from tqdm import tqdm

# Load the dataset
df = pd.read_csv(r'C:\Users\SHAMEER.K\OneDrive\Desktop\ml challenge\student_resource 3\dataset\train.csv')

# Create a directory to save images if it doesn't exist
os.makedirs('images', exist_ok=True)

# Function to download an image from the URL
def download_image(url, image_id, folder='images'):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder, f"{image_id}.jpg"), 'wb') as f:
            f.write(response.content)

# Iterate over the dataframe rows
for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    image_link = row['image_link']
    
    # Use row index as image ID
    image_id = index

    # Download image
    try:
        download_image(image_link, image_id)
    except Exception as e:
        print(f"Failed to download image {image_id}: {e}")
