import os
import shutil

def import_images(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through the files in the source directory
    for filename in os.listdir(source_dir):
        # Check if the file is an image based on the file extension
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Get the full path of the source file
            source_path = os.path.join(source_dir, filename)

            # Create a new directory with the image extension
            extension = os.path.splitext(filename)[1]
            image_dir = os.path.join(destination_dir, extension[1:].upper())
            os.makedirs(image_dir, exist_ok=True)

            # Generate a unique filename for the image
            count = 1
            base_name = os.path.splitext(filename)[0]
            new_filename = filename
            while os.path.exists(os.path.join(image_dir, new_filename)):
                new_filename = f"{base_name}_{count}{extension}"
                count += 1

            # Copy the image to the destination directory
            destination_path = os.path.join(image_dir, new_filename)
            shutil.copyfile(source_path, destination_path)

            print(f"Imported: {filename} -> {destination_path}")

# Example usage
source_directory = '/path/to/source'
destination_directory = '/path/to/destination'

import_images(source_directory, destination_directory)
