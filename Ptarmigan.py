# This is the PIL library
from PIL import Image

# This is the argparse library for command-line argument
import argparse

# This is the os library, which is used to check os path of user's input
import os

# This re library handles regular expressions
import re

# This is the sys library which is used to exit program when a check returns False
import sys


def main():
    # Instantiating ArgumentParser object from the argparse module
    parser = argparse.ArgumentParser(description="handle file input in command-line application")
    parser.add_argument("-f", help="image upload file path")
    parser.add_argument("-l", nargs="+", help="list of images for an animated gif")
    parser.add_argument("-o", help="Image format you want to convert to")
    parser.add_argument("-n", help="Name of the new file you want to create")
    args = parser.parse_args()


    #Initializing user input file by assigning args.f to a variable
    input_file = args.f
    r, e= os.path.splitext(input_file)
    input_file = f"{r}{e.lower()}"


    # Calling the check_none and check_extensions on file_path
    check_none(input_file, "Input either a .png, .jpeg, .jpg, or .gif file")
    check_extensions(input_file, [".png", ".jpg", ".jpeg", ".gif"], "Input file must be either .png, .jpg, .jpeg, or .gif")


    # Initializing image file list to a variable
    image_list = args.l


    # Continuing program if image_list is empty and calling check_extensions() on image_list
    if image_list is not None:
        for i in image_list:
            check_extensions(i, [".png", ".jpg", ".jpeg"], "list of image files must be in the .png, .jpg, .jpeg format.")


    # Initializing output format by assigning args.o to a variable
    output_format = args.o


    # Handling instance when output_file is equivalent to None and calling check_extensions() on output_file
    root, extension = os.path.splitext(input_file)
    if output_format == None:
        output_format = extension

    output_format = output_format.lower()
    if not output_format.endswith((".png", ".jpeg", ".jpg", ".gif")):
        sys.exit("Can only convert image file to either .png, .jpeg, .jpg, or .gif")


    # initializing name of output file by assigning args.n to a variabe
    output_name = args.n


     # Checking if args.n is provided
    if output_name is None:
        default = input_file.split(".")
        output_name = default[0]


    # Ensuring output_name is a string by converting it to a str
    output_name = str(output_name)
    output_name = output_name.lower()


    # Checking if args.n has an extension
    if "." in output_name:
        first, last = os.path.splitext(output_name)
        output_name = first


    # Checking that output_name matches intended format using regular expressions checks
    pattern = r"^[A-Za-z0-9_]+$"
    if not re.match(pattern, output_name):
        sys.exit("Invalid output_name format. Only alpha-numeric characters, and underscores are allowed.")


    # Coverting .PNG, .JPEG, or .JPG image file to either .PNG, .JPEG, or .JPG
    if input_file.endswith((".png",".jpg",".jpeg")) and output_format in (".png",".jpg",".jpeg"):
        print(same_image_converter(input_file, output_format, output_name))


    # Converting .GIF image file to either .PNG, .JPEG, or .JPG
    if input_file.endswith(".gif") and output_format in (".png",".jpg",".jpeg"):
        print(gif_converter(input_file, output_format, output_name))


    # converting from (.PNG, .JPG, .JPEG) to static GIF. (If image_list is empty and output_file extension is equivalent to GIF)
    if image_list == None and output_format == ".gif":
        print(convert_2_static_gif(input_file, output_format, output_name))


    # Converting .PNG, .JPEG, or .JPG image file to animated GIF
    if input_file.endswith((".png",".jpg","jpeg")) and image_list is not None and output_format == ".gif":
        print(convert_2_animated_gif(input_file, image_list, output_format, output_name))


    # Displaying all object instances as outputs
    print(f"Input_file ={input_file}, image_list={image_list} output_name={output_name}, output_format={output_format}")


# Defining a function that checks if command-line arguments is equivalent to None
def check_none(arg, message):
    if arg == None:
        sys.exit(message)


# Defining a function that checks for file path / extensions
def check_extensions(file, valid_extensions, message):
    root, extension = os.path.splitext(file)
    if extension not in (valid_extensions):
        sys.exit(message)


# Defining image_file_converter for .PNG to .JPEG categories
def same_image_converter(input_, output_, output_name):
    output = output_.lstrip(".").upper()
    if output == "GIF":
        sys.exit("Can't convert to .gif")
    try:
        if output == "JPG":
            output = "JPEG"
        img = Image.open(input_)
        if output == "JPEG":
            img = img.convert("RGB")
        new_image = f"{output_name}.{output.lstrip(".").lower()}"
        img.save(new_image, format=output)
        return f"Image successfully converted"
    except IOError:
        sys.exit("Could not open nor save file")


# Defining function for converting GIF to either .PNG, .JPEG, or .JPG
def gif_converter(input_, output_, output_name):
    one, two = os.path.splitext(input_)
    if two.lower() != ".gif":
        sys.exit("Input file must be a gif file")
    output = output_.lstrip(".").upper()
    if output == "GIF":
        sys.exit("Can only convert to either of .png, .jpg, and .jpeg")
    if output == "JPG":
        output = "JPEG"
    img = Image.open(input_)
    new_image = f"{output_name}.{output.lstrip(".").lower()}"
    img.seek(0)
    if output == "JPEG":
        img = img.convert("RGB")
    img.save(new_image, format=output)
    return f"Image successfully converted"


# Defing function that convert image format to static GIF
def convert_2_static_gif(input1, output_, output_name):
    one, two = os.path.splitext(input1)
    if two.lower() == ".gif":
        sys.exit("Unsupported format. Input file can't be a gif")
    output = output_.lstrip(".").upper()
    if output != "GIF":
        sys.exit("Can only convert to a static gif")
    img = Image.open(input1)
    if two == "JPG":
        two = "JPEG"
    new_image = f"{output_name}.{output.lower()}"
    img.save(new_image)
    return f"Image successfully converted"


# Defining a function that converts a list of either .JPG, .PNG, .JPEG image files to an animated GIF
def convert_2_animated_gif(input1, input2, output_, output_name):
    # Ensuring that input1 is in the supported format
    one, two = os.path.splitext(input1)
    if two.lower() == ".gif":
        sys.exit("Unsupported format. Input file can't be a gif")

    # Removing the "." in output_ to match the .save format, initializing an empty list, and accessing images via .open
    output = output_.lstrip(".").upper()
    if output != "GIF":
        sys.exit("Can only convert to a static gif")
    pictures = []
    imgs = [Image.open(input1)] + [Image.open(pic) for pic in input2]

    # Handling case where the extension of both input1 and input2(list) is .jpg
    if two.lower() == ".jpg":
        two = ".jpeg"
    input2 = [os.path.splitext(pic)[0] + ".jpeg" if os.path.splitext(pic)[1].lower() == ".jpg" else pic for pic in input2]

    # Calculating size(width, height) of image files in input1 and input2, then resizing image files and appending them to the empty list
    width, height = imgs[0].size
    for img in imgs:
        img = img.resize((width, height))
        pictures.append(img)
    new_image = output_name + "." + output.lower()

    # Saving the list of newly sized image_file, and creating an animated gif
    pictures[0].save(
        new_image, save_all=True, append_images=pictures[1:], duration=200, loop=5
    )
    return f"Image successfully converted"


if __name__ == "__main__":
    main()
