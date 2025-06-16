from flask import request, jsonify
from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def image_to_ascii(image, width=100):
    image = image.convert("L")
    aspect_ratio = image.height / image.width
    height = int(aspect_ratio * width * 0.55)
    image = image.resize((width, height))

    pixels = image.getdata()
    ascii_str = ''.join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return '\n'.join(ascii_str[i:i+width] for i in range(0, len(ascii_str), width))


def ascii_upload():
    file = request.files.get("image")
    if not file:
        return jsonify({"error": "No file provided"}), 400
    try:
        image = Image.open(file.stream)
        ascii_art = image_to_ascii(image)
        return jsonify({"ascii": ascii_art})
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500
