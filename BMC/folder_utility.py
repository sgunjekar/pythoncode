import os
import shutil

# Set the path to your source folder (e.g., Downloads)
source_folder = r"This PC\sushil's S21 Ultra\Internal storage\DCIM\Camera"  # Change as needed

# Destination folders
videos_folder = os.path.join(source_folder, "Videos")
pics_folder = os.path.join(source_folder, "Pics")

# Create destination folders if they don't exist
os.makedirs(videos_folder, exist_ok=True)
os.makedirs(pics_folder, exist_ok=True)

# Video and image file extensions
video_exts = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv')
image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')

# Go through files in the folder
for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)

    # Skip folders
    if not os.path.isfile(filepath):
        continue

    # Move video files
    if filename.lower().endswith(video_exts):
        shutil.move(filepath, os.path.join(videos_folder, filename))
        print(f"Moved video: {filename}")

    # Move image files
    elif filename.lower().endswith(image_exts):
        shutil.move(filepath, os.path.join(pics_folder, filename))
        print(f"Moved image: {filename}")
