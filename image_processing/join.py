from PIL import Image

def join_images(image1_path, image2_path, output_path, target_height):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Calculate the aspect ratio for each image
    aspect_ratio1 = image1.width / image1.height
    aspect_ratio2 = image2.width / image2.height

    # Calculate the new width for each image to match the target height
    new_width1 = int(target_height * aspect_ratio1)
    new_width2 = int(target_height * aspect_ratio2)

    # Resize both images to have the same height
    image1 = image1.resize((new_width1, target_height))
    image2 = image2.resize((new_width2, target_height))

    # Concatenate images horizontally
    joined_image = Image.new('RGB', (new_width1 + new_width2, target_height))
    joined_image.paste(image1, (0, 0))
    joined_image.paste(image2, (new_width1, 0))

    # Save the joined image
    joined_image.save(output_path)

# Example usage
image1_path = "image1.png"
image2_path = "image2.png"
output_path = "joined_image.png"
target_height = 225  # specify the target height for the resized images

join_images(image1_path, image2_path, output_path, target_height)