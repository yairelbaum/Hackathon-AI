from image_import import import_images
from image_classification import classify_image
from image_printing import print_classified_picture

def main():
    # Step 1: Import images
    source_directory = '/path/to/source'
    destination_directory = '/path/to/destination'
    import_images(source_directory, destination_directory)

    # Step 2: Classify and print images
    image_path = '/path/to/destination/dog/image.jpg'
    predicted_class = classify_image(image_path)
    print_classified_picture(image_path, predicted_class)

if __name__ == "__main__":
    main()
