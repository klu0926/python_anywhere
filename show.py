# this use the 'sample-avatar.jpg' in the project folder


# importing image class from PIL package
from PIL import Image

# creating image object
img = Image.open(r"/Users/lukuoyu/Desktop/humber/python/ascii_art/sample-avatar.jpg")

# using convert method for img1
img1 = img.convert("L")
img1.show()