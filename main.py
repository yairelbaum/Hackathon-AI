import argparse
from classify import classify_image
from alter_photo import title_to_image

# Adding resNet mapping from id to name of animal
mapping = {101: "elephant", 339: "horse", 145: "penguin", 207: "dog"}

def parse_arguments():
    """
    parse program arguents
    """
    parser = argparse.ArgumentParser(description="Get changed files in a Git repository")
    # Add the repository path argument
    parser.add_argument("-i", "--image", type=str, help="Path to image", required=True)
    # Parse the command-line arguments
    return parser.parse_args()

def main():
    # Step 1: Import images
    args = parse_arguments()    

    # Step 2: Predict the image
    predicted_class = mapping[classify_image(args.image)]
    print(predicted_class)

    # Step 3: Add title to image and save as new image
    new_file_name = args.image.split(".png")[0] + "taged.png"
    title_to_image(args.image, predicted_class, new_file_name)

if __name__ == "__main__":
    main()
