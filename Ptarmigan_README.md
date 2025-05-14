# Ptarmigan

###
VIDEO DEMO <https://youtu.be/vMe-JiYdnEk?feature=shared>
DESCRIPTION: Ptarmigan is a command-line Image conversion program, capable of converting Images from one format to another, based off
the users specification. This command-line application is structured to take in multiple arguments depending on what task a user intend the
program to carry out.
    Part of the structure of the Ptarmigan application is the argparse library, which ensures efficiency in parsing multiple command-line ar-
guments. Another library that Ptarmigan operates with is Image from PIL module via PIP-installed Pillow. This library focuses on the effect-
ive opening, modifying, and saving of image files, which is pivotal to the successful conversion from one image format to another. Ptarmigan
also capitalizes on the os library which is used to checked the path extension of image file, which enables the program to moderate the prop-
erties of each command-line objects, and systematically exit via the sys library, when the path extension of any argument(file) does not match
the supported image file format stipulated by the program. Ptarmigan also uses the re library to construct regular expression pattern that
is used to check certain command-line argument.
    There're a total of four(4) command-line arguments in this program, although not all are always required for certain functionality of
the program. The first command-line argument is the args.f(-f), which is initialized to the input_file variable. This input_file represents the p-
rimary image file that must be present in other for there to be any conversion of formats, i.e to say the program would exit if input_file is
not provided. The second command-line argument is args.l(-l), which is a list of image files initialized to the image_list variable. This command-line
argument is only required when multiple images are to be modified and converted, thereby making it optional. The third command-line argument is args.o(-o), 
which is a path extension that specifies the format that a user intends to convert to, the args.o is initialized to the output_format variable, and would 
automatically be assigned the extension of the input_file(args.f) in the case where output_farmat is absent. Finally is the args.n(-n) command-line argument. 
This argument is initialized to the output_name variable, and it assigns a name to the newly converted image, and in the case where the args.n is not provided, 
the program is structured to assign the name of the input_file(args.f) to  the newly converted image.
    The Ptarmigan application has six(6) functions, namely check_none(), check_extensions(), same_image_converter(),gif_converterconvert_2_static
_gif(), convert_2_animated_gif(). The check_none() function handles the check for the availabilty or absence of arguments(image_files), and determines 
if the program continues or exit based on if certain conditions return True or False. The check_extensions() function is responsible for checking the file path 
extensions of arguments(image files), exiting program with an error message if the path extension does not match the expected and supported image file format. 
The same_image_converter() function handles the conversion of image files from either .png, .jpg, or .jpeg to either .jpg, .jpeg, or .png. The gif_converter() function,
converts gif image file to either .jpeg, .png, or .jpg depending on user's specification. The convert_2_static_gif() function converts .png, .jpeg, or .jpg image files 
to static gifs. last but not the least, the convert_2_animated_gif() function, handles the conversion of multiple .png, .jpg, and .jpeg image files to animated gifs.
    Only .png, .jpeg, .gif, .jpg image files are supported by Ptarmigan, any other file if passed as argument, would lead to program exiting. I
initially wanted a program that takes in an image file as command-line argument, and then process, and return the encyclopedia of inputted image, much like google lens, 
but I couldn't get the vision cloud API clearance due to what's starting to look like an unresolvble issue with my billing account on my Google services account. 
I then opted to try the IIIF API, it turned out it doesn't handle label, text, face, logo, landmark, nor web detection like Vision cloud API, and after encountering numerous
obstacles with sychronizing the loris IIIF server with my program, on a cloud based coding enviroment(cs50.dev), I reverted back to the Pillow library, considering it does
every other thing the IIIF API does. I'm super excited to finally finalize the Ptarmigan, as my project on cs50 introduction to programming with python.

## Usage

To run the program, use the following command:

To call the gif_converter() function:
```
python project.py -f bear.gif -o .jpeg
```
To call the convert_2_static_gif() function:
```
python project.py -f capture.png -o .gif
```
To call the convert_2_animated_gif() functiom:
```
python project.py -f animal.png -l bear.png download1.jpeg download2.jpeg download3.jpeg -o .gif -n nature.gif
```
To call same_image_converter() function:
```
python project.py -f capture.png -o .jpg
```
To run pytest program on test_project.py:
```
pytest test_project.py
```
###
