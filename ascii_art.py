# Preparing libraries for image processing
from PIL import Image
import numpy as np

# Read the image 
img = Image.open("ww.jpeg") # Initialize variable named "img" with Image class from PIL

# Display the image
# image.show()

# 2. Load your image’s pixel data into a 2-dimensional array
# Initialize values for image's width and height
img_width = img.width
img_height = img.height
img_pixel = img_width * img_height


# To get a pixel data, iterate through image's width and height
img_pixel_rgb = np.zeros((3, img_height, img_width))

for channel in range(len(img_pixel_rgb)): # represents the channel iterator
    for y in range(len(img_pixel_rgb[0])): # represents the y point iterator
        for x in range(len(img_pixel_rgb[0][0])): # represents the x point iterator
            img_pixel_rgb[channel][y][x] = img.getpixel((x,y))[channel]

# 3. Convert the RGB pixels into single brightness pixels
# by using the average method: (R + G + B) / 3
img_pixel_brightness = np.zeros((img_height, img_width), dtype="int32") # initialize a variable that stores brightness pixels

for y in range(len(img_pixel_brightness)): # represents the y point iterator
    for x in range(len(img_pixel_brightness[0])): # represents the x point iterator
        img_pixel_brightness[y][x] = (sum(img.getpixel((x,y)))) // 3

# 4. Convert brightness numbers to ASCII characters

ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
print(len(ascii_chars))




