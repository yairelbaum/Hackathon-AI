from PIL import Image, ImageDraw, ImageFont

def title_to_image(image_path, title, output_path):
    # Open the image
    image = Image.open(image_path)

    # Create a blank image with the same size as the original image
    modified_image = Image.new(image.mode, image.size)

    # Copy the original image to the modified image
    modified_image.paste(image)

    # Calculate the position to place the title
    title_position = (10, 10)  # Adjust the position as per your requirements

    # Create a draw object
    draw = ImageDraw.Draw(modified_image)

    # Specify the font size and style
    font_size=30
    font = ImageFont.truetype("/mnt/c/Windows/Fonts/arial.ttf", font_size)  # Adjust the font and its path as per your requirements

    # Draw the title on the modified image
    draw.text(title_position, title, font=font, fill=(132, 218, 43))  # Adjust the fill color as per your requirements

    # Save the modified image
    modified_image.save(output_path)