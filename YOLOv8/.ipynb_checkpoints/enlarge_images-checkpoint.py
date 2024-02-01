#make sure to do pip install Pillow

from PIL import Image
import os

def resize_images(input_output_folder, target_size=(640, 640)):
    # Ensure the folder exists
    os.makedirs(input_output_folder, exist_ok=True)

    # List all files in the folder
    input_files = os.listdir(input_output_folder)

    for filename in input_files:
        input_path = os.path.join(input_output_folder, filename)
        output_path = os.path.join(input_output_folder, filename)

        # Open the image
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize(target_size, resample=Image.LANCZOS)

            # Save the resized image
            resized_img.save(output_path)

    print(f'Finished resizing {len(input_files)} images.')

# Example usage:
folder = 'datasets/data/train/images'
resize_images(folder, folder)
folder = 'datasets/data/train/labels'
resize_images(folder)
folder = 'datasets/data/test/images'
resize_images(folder)
folder = 'datasets/data/test/labels'
resize_images(folder)
