import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

def read_image(image_path):
    """  Read an image from the specified path """
    img = cv2.imread(image_path)
    return img

def display_image(img, title='Image'):
    """  Display the image using matplotlib """
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def convert_to_grayscale(img):
    """  Convert the image to grayscale """
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

def apply_blur(img, kernel_size=(5, 5)):
    """  Apply Gaussian blur to the image """
    blurred_img = cv2.GaussianBlur(img, kernel_size, 0)
    return blurred_img

def edge_detection(img, low_threshold=50, high_threshold=150):
    """  Apply Canny edge detection to the image """
    edges = cv2.Canny(img, low_threshold, high_threshold)
    return edges

def resize_image(img, new_size=(300, 300)):
    """  Resize the image to the specified dimensions """
    resized_img = cv2.resize(img, new_size)
    return resized_img

def adjust_brightness_contrast(img, alpha=1.5, beta=30):
    """  Adjust the brightness and contrast of the image """
    adjusted_img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return adjusted_img

def apply_threshold(img, threshold_value=128, max_value=255, threshold_type=cv2.THRESH_BINARY):
    """  Apply a binary threshold to the image """
    _, thresholded_img = cv2.threshold(img, threshold_value, max_value, threshold_type)
    return thresholded_img

def apply_dilation(img, kernel_size=(5, 5)):
    """  Apply dilation to the image """
    kernel = np.ones(kernel_size, np.uint8)
    dilated_img = cv2.dilate(img, kernel, iterations=1)
    return dilated_img

def change_image_color(img, channel, value):
    """  Change the intensity of a specific color channel """
    img_copy = img.copy()
    img_copy[:, :, channel] += value
    return img_copy

def find_and_draw_contours(img):
    """  Find contours in the image and draw them """
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    return contour_img

def most_used_color(img):
    """  Reshape the image to a 2D array of pixels """
    pixels = img.reshape((-1, 3))
    
    # Convert to a list of [B, G, R] values
    pixels = pixels.tolist()
    
    # Count occurrences of each color
    color_counts = {}
    for pixel in pixels:
        color = tuple(pixel)
        color_counts[color] = color_counts.get(color, 0) + 1
    
    # Find the color with the maximum occurrence
    most_used_color = max(color_counts, key=color_counts.get)
    return most_used_color

def image_details(img):
    """  Get image dimensions """
    height, width, channels = img.shape
    
    # Get pixel values for the center and four corners
    center_pixel = img[height // 2, width // 2]
    top_left_pixel = img[0, 0]
    top_right_pixel = img[0, width - 1]
    bottom_left_pixel = img[height - 1, 0]
    bottom_right_pixel = img[height - 1, width - 1]
    
    return {
        'Image Dimensions': (height, width, channels),
        'Center Pixel Value': center_pixel,
        'Top Left Pixel Value': top_left_pixel,
        'Top Right Pixel Value': top_right_pixel,
        'Bottom Left Pixel Value': bottom_left_pixel,
        'Bottom Right Pixel Value': bottom_right_pixel
    }
    
def image_to_ascii(img, scale_factor=0.1):
    # If img is a string (file path), read the image
    if isinstance(img, str):
        img = cv2.imread(img)

    # Check if the image is loaded successfully
    if img is None:
        print("Error: Could not open image.")
        return

    # Resize the image for better ASCII representation
    small_img = cv2.resize(img, (0, 0), fx=scale_factor, fy=scale_factor)

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2GRAY)

    # Define ASCII characters for different intensity levels
    ascii_chars = "@%#*+=-:. "

    # Normalize pixel values to the range [0, len(ascii_chars))
    normalized_pixels = ((gray_img / 255) * (len(ascii_chars) - 1)).astype(np.uint8)

    # Convert pixel values to ASCII characters
    ascii_art = ""
    for row in normalized_pixels:
        for pixel_value in row:
            ascii_art += ascii_chars[pixel_value]
        ascii_art += "\n"

    return ascii_art


def extract_text_from_image(image_path,tesseract_path):
    """
    Extracts text from an image using Optical Character Recognition (OCR) with Tesseract.

    Args:
        image_path (str): The file path to the image from which text needs to be extracted.
        tesseract_path (str): The file path to the Tesseract executable.

    Returns:
        str: The extracted text from the image.
    """
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    # Open the image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

def rotate_image(img, angle):
    """Rotate the image by a specified angle."""
    rows, cols, _ = img.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (cols, rows))
    return rotated_img

def apply_mask(img, mask):
    """Apply a binary mask to the image."""
    masked_img = cv2.bitwise_and(img, img, mask=mask)
    return masked_img

def invert_image(img):
    """Invert the colors of the image."""
    inverted_img = cv2.bitwise_not(img)
    return inverted_img

def add_noise(img, intensity=50):
    """Add random noise to the image."""
    noise = np.random.normal(0, intensity, img.shape)
    noisy_img = img + noise
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)
    return noisy_img

def morphological_operations(img, operation='dilate', kernel_size=(5, 5)):
    """Apply morphological operations to the image."""
    kernel = np.ones(kernel_size, np.uint8)
    if operation == 'dilate':
        result_img = cv2.dilate(img, kernel, iterations=1)
    elif operation == 'erode':
        result_img = cv2.erode(img, kernel, iterations=1)
    else:
        raise ValueError("Invalid operation. Use 'dilate' or 'erode'.")
    return result_img
