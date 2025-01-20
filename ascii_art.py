# Preparing libraries for image processing
from PIL import Image
import numpy as np

def ascii_chars_separator(string):
    arr_of_chars = []
    for i in string:
        arr_of_chars.append(i)

    return arr_of_chars

def ranged_int_to_char(ascii_chars, comparator, integers):
    converted_integers = {}

    for i in range(len(comparator)):
    # for i in range(len(comparator) - 1):
        if i == len(comparator) - 1: # the last char will be iterated
            for j in range(comparator[i-1], comparator[i]): # we have to use range from the second latest num to the latest num + 1 
            # because stop won't be stepped
                if integers[j] >= comparator[i-1] and integers[j] <= comparator[i]:
                    # converted_integers.append(ascii_chars[i])
                    converted_integers[j] = ascii_chars[i]
        else:
            for j in range(comparator[i], comparator[i+1]): # the last char won't be iterated
                if integers[j] >= comparator[i] and integers[j] < comparator[i+1]:
                    # converted_integers.append(ascii_chars[i])
                    converted_integers[j] = ascii_chars[i]
    
    return converted_integers

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
# BEGIN
ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
print(len(ascii_chars))
comparator = np.linspace(0, 255, len(ascii_chars), dtype="int32")
integers = np.linspace(0, 255, 256, dtype="int32")

print(ranged_int_to_char(ascii_chars, comparator, integers))

# 5. Print the ASCII art


