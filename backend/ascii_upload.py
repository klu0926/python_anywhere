from flask import request, jsonify
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

# Convert image to ascii
def image_to_ascii(image, width=100):
    
    # Conver to grayscal
    image = image.convert("L")

    # Calcualte aspect ratio
    aspect_ratio = image.height / image.width

    # make image's height shorter, as character's height is longer than width. This make the ascii art ratio looks normal
    height = int(aspect_ratio * width * 0.55)
    image = image.resize((width, height))

    # Get each pixel 
    pixels = image.getdata()

    # Create chars with each pixel, pick ASCII_CHARS 
    # with 10 level of brighness (0 - 9) by floor divid with 25 (grayscale pixel at 255) 
    # "min" to ensure its never out of range when grayscale is at 255, whcih will result a 10 in index out of 9
    ascii_str = ''.join(ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in pixels)

    # Seperate chars by image width, and concate with '\n' to create the ASCII image
    return '\n'.join(ascii_str[i:i+width] for i in range(0, len(ascii_str), width))


# Return ascii
def return_ascii():
    # Get image file from request form data
    file = request.files.get("image")

     # Get the width from formData, convert to int
    width = request.form.get("width", default=100, type=int)

    if not file:
        return jsonify({"error": "No file provided"}), 400
    
    try:
        # open the image with stream
        image = Image.open(file.stream)

        ascii_art = image_to_ascii(image, width)
        return jsonify({"ascii": ascii_art})
    
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500
