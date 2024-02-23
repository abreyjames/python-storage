from PIL import Image


def print_image_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            print("Image Resolution for:", image_path)
            print("Width:", width)
            print("Height:", height)
    except Exception as e:
        print("Error:", e)


def crop_image(image_path, top_left, bottom_right):
    # Open the image
    image = Image.open(image_path)

    # Crop the image
    cropped_image = image.crop(
        (top_left[0], top_left[1], bottom_right[0], bottom_right[1]))

    # Save the cropped image
    output_path = image_path.split('.')[0] + '_crop.' + image_path.split('.')[1]
    cropped_image.save(output_path)

    return cropped_image


# Example usage:
if __name__ == "__main__":
    image_path = input("Enter the path to the image file: ")
    top_left_x = int(input("Enter the x-coordinate of the top left corner: "))
    top_left_y = int(input("Enter the y-coordinate of the top left corner: "))
    bottom_right_x = int(
        input("Enter the x-coordinate of the bottom right corner: "))
    bottom_right_y = int(
        input("Enter the y-coordinate of the bottom right corner: "))

    top_left = (top_left_x, top_left_y)
    bottom_right = (bottom_right_x, bottom_right_y)

    cropped_image = crop_image(image_path, top_left, bottom_right)
    print("Image cropped and saved successfully.")
