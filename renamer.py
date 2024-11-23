import os

def rename_images(folder_path, prefix="24102023_"):
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg'))]
    
    images.sort()
    
    for index, file_name in enumerate(images, start=1):
        old_path = os.path.join(folder_path, file_name)
        new_name = f"{prefix}{index}.jpg"  
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")

# Usage
folder_path = "sanitary_towels_drive_24102023" 
rename_images(folder_path)
