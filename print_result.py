# Function to print the classified picture
def print_classified_picture(image_path, predicted_label):
    image = Image.open(image_path)
    image.show()
    print(f"Predicted label: {predicted_label}")
    print("------------------------------------------------------")
