from PIL import Image
import numpy as np

def change_color(image_path, target_color, replacement_color, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Define the target color (RGB format)
    target_color = tuple(target_color)

    # Create a mask of pixels that match the target color
    mask = np.all(img_array[:, :, :3] == target_color, axis=-1)

    # Replace the target color with the replacement color
    img_array[mask, :3] = replacement_color

    # Convert the NumPy array back to an image
    new_img = Image.fromarray(img_array)

    # Save the modified image
    new_img.save(output_path)

if __name__ == "__main__":
    # Replace 'your_icon.png' with the path to your PNG clip art icon image
    icon_path = 'banshee_logo.png'

    # Specify the target color to be replaced (in RGB format)
    target_color = (255, 255, 255)  # Example: white color

    # Specify the replacement color (in RGB format)
    replacement_color = (255, 0, 0)  # Example: red color

    # Replace 'output_icon.png' with the desired output path
    output_path = 'output_icon.png'

    # Call the function to change the color
    change_color(icon_path, target_color, replacement_color, output_path)
