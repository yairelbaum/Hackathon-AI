from classify import classify_image
# from image_classification import classify_image
# from image_printing import print_classified_picture

def main():
    # Step 1: Import images
    image_path = 'elephant.png'
    # destination_directory = '/path/to/destination'
    # import_images(source_directory, destination_directory)
    

    predicted_class = classify_image(image_path)
    print(predicted_class)
    # print_classified_picture(image_path, predicted_class)

if __name__ == "__main__":
    main()
