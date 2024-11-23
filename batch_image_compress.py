import os
from PIL import Image

print('Starting ...')
def batch_compress(input_folder, output_folder, quality=75, resize_percent=None):
    os.makedirs(output_folder, exist_ok=True) 

    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.jpg', '.jpeg')): 
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            with Image.open(input_path) as img:
                img = img.convert("RGB")  #compatibility for compression
                
                # Resizing
                if resize_percent:
                    width = int(img.width * resize_percent / 100)
                    height = int(img.height * resize_percent / 100)
                    img = img.resize((width, height), Image.Resampling.LANCZOS)
                
                # Compress and save as JPG
                img.save(output_path, "JPEG", optimize=True, quality=quality)
                print(f"Compressed: {file_name} -> Saved to {output_path}")

input_folder = "blog_thumbnail"
output_folder = "blog_thumbnail/compressed"
batch_compress(input_folder, output_folder, quality=70, resize_percent=70)  
