# 0. Preparing libraries for image processing
from PIL import Image
import numpy as np

# User-defined functions
def get_pixel(img):
    img_height = img.height
    img_width = img.width
    img_pixel_rgb = np.zeros((3, img_height, img_width))

    for channel in range(len(img_pixel_rgb)): # represents the channel iterator
        for y in range(len(img_pixel_rgb[0])): # represents the y point iterator
            for x in range(len(img_pixel_rgb[0][0])): # represents the x point iterator
                img_pixel_rgb[channel][y][x] = img.getpixel((x,y))[channel]

    return img_pixel_rgb

def img_to_brightness_pixel(img):
    img_height = img.height
    img_width = img.width
    img_pixel_brightness = np.zeros((img_height, img_width), dtype="int32") # initialize a variable that stores brightness pixels

    for y in range(len(img_pixel_brightness)): # represents the y point iterator
        for x in range(len(img_pixel_brightness[0])): # represents the x point iterator
            img_pixel_brightness[y][x] = (sum(img.getpixel((x,y)))) // 3

    return img_pixel_brightness

def encoding_int_to_char(ascii_chars):
    comparator = np.linspace(0, 255, len(ascii_chars), dtype="int32")
    rgb_interval = np.linspace(0, 255, 256, dtype="int32")
    converted_integers = {}

    for i in range(len(comparator)):
    # for i in range(len(comparator) - 1):
        if i == len(comparator) - 1: # the last char will be iterated
            for j in range(comparator[i-1], comparator[i] + 1): # we have to use range from the second latest num to the latest num + 1 
            # because stop won't be stepped
                if rgb_interval[j] >= comparator[i-1] and rgb_interval[j] <= comparator[i]:
                    # converted_integers.append(ascii_chars[i])
                    converted_integers[j] = ascii_chars[i]
        else:
            for j in range(comparator[i], comparator[i+1]): # the last char won't be iterated
                if rgb_interval[j] >= comparator[i] and rgb_interval[j] < comparator[i+1]:
                    # converted_integers.append(ascii_chars[i])
                    converted_integers[j] = ascii_chars[i]
    
    return converted_integers

def brightness_to_ascii(brightness, encoder, multiply = 1):
    ascii_image = []

    for y in range(len(brightness)): # represents the y point iterator
        for x in range(len(brightness[0])): # represents the x point iterator
           for key in encoder:
                if brightness[y][x] == key:
                    if multiply > 1:
                        char = encoder[key]
                        new_char = ""
                        for i in range(multiply):
                            new_char = new_char + char
                        ascii_image.append(new_char)
                    else:
                        ascii_image.append(encoder[key])

    ascii_image = np.array(ascii_image)
    ascii_image = np.reshape(ascii_image, (len(brightness), len(brightness[0])))

    return ascii_image

def display_ascii_image(ascii_image):
    for y in range(len(ascii_image)):
        for x in range(len(ascii_image[0])):
            print(ascii_image[y][x], end="")
        print()

def save_as_txt(filename, ascii_image):
    try:
        ascii_image_txt = open(filename, 'x') # Create
        ascii_image_txt = open(filename, 'a')
        for i in range(len(ascii_image)):
            for j in range(len(ascii_image[0])):
                ascii_image_txt.write(ascii_image[i][j])
            ascii_image_txt.write("\n")

        ascii_image_txt.close()
    except:
        print("The file with that name has been created. Please change the filename!")

# 1. Read the image 
# BEGIN
img = Image.open("ww.jpeg") # Initialize variable named "img" with Image class from PIL
# img = img.resize((img.width // 2, img.height // 2)) To resize the image

# END

# 2. Load your image’s pixel data into a 2-dimensional array
# Initialize values for image's width and height
# BEGIN

# To get a pixel data, iterate through image's width and height
img_pixel_rgb = get_pixel(img)
# END

# 3. Convert the RGB pixels into single brightness pixels
# by using the average method: (R + G + B) / 3
img_pixel_brightness = img_to_brightness_pixel(img)

# 4. Convert brightness numbers to ASCII characters
# BEGIN
ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
encoder = encoding_int_to_char(ascii_chars)

ascii_image = brightness_to_ascii(img_pixel_brightness, encoder, 2)
# END

# 5. Print the ASCII art
# BEGIN
display_ascii_image(ascii_image)
# END

# 6. Save the ASCII art as .txt file
save_as_txt("ww.txt", ascii_image)


