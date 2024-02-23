from PIL import Image

def add_whitespace_to_top(image_path, target_height, output_path):
    # Open the image
    image = Image.open(image_path)

    # Get the current dimensions of the image
    width, height = image.size

    # Check if the height of the image is less than the target height
    if height < target_height:
        # Calculate the amount of whitespace needed
        whitespace_height = target_height - height

        # Create a new image with the desired dimensions
        new_image = Image.new('RGB', (width, target_height), color='white')

        # Paste the original image onto the new image with the whitespace at the top
        new_image.paste(image, (0, whitespace_height))
    else:
        # If the image height is already larger or equal to the target height, no whitespace needed
        new_image = image

    # Save the modified image
    new_image.save(output_path)

# Example usage
image_path = "image1.png"
target_height = 10  # specify the target height for the modified image
output_path = "output_image.jpg"

add_whitespace_to_top(image_path, target_height, output_path)
