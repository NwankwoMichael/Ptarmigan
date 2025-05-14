from project import check_none

from project import check_extensions

from project import same_image_converter

from project import gif_converter

from project import convert_2_static_gif

from project import convert_2_animated_gif

import pytest


# Testing the check_none function
def test_check_none():
    with pytest.raises(SystemExit):
        check_none(None, "Input either a .png, .jpeg, .jpg, or .gif file")


# Testing the check_extensions function
def test_check_extensions():
    with pytest.raises(SystemExit):
        check_extensions("apple.text", [".png", ".jpg", ".jpeg", ".gif"], "Input file must be either .png, .jpg, .jpeg, or .gif")


# Testing the same_image_converter function
def test_same_image_converter():
    assert same_image_converter("animal.jpg", ".png", "animal") == "Image successfully converted"
    assert same_image_converter("capture.png", ".jpeg", "imagery") == "Image successfully converted"
    assert same_image_converter("bear.png", ".jpg", "bear") == "Image successfully converted"
    with pytest.raises(SystemExit):
        same_image_converter("loner.mp4", ".jpeg", "loner")
    with pytest.raises(SystemExit):
        same_image_converter("download1.jpeg", ".gif", "download")

# Testing the gif_converter function
def test_gif_converter():
    assert gif_converter("animal.gif", ".png", "fun") == "Image successfully converted"
    assert gif_converter("bear.gif", ".jpg", "fun") == "Image successfully converted"
    assert gif_converter("nature.gif", ".jpeg", "fun") == "Image successfully converted"
    with pytest.raises(SystemExit):
        gif_converter("animal.jpg", ".png", "anime")

# Testing the convert_2_static_gif function
def test_convert_2_static_gif():
    assert convert_2_static_gif("download2.jpeg", ".gif", "static") == "Image successfully converted"
    assert convert_2_static_gif("bear.png", ".gif", "static") == "Image successfully converted"
    assert convert_2_static_gif("animal.jpg", ".gif", "static") == "Image successfully converted"
    with pytest.raises(SystemExit):
        convert_2_static_gif("nature.gif", ".gif", "nature")
    with pytest.raises(SystemExit):
        convert_2_static_gif("download1.jpeg", ".png", "nature")


# Testing the convert_2_animated_gif function
def test_convert_2_animated_gif():
    assert convert_2_animated_gif("animal.jpg", ["bear.png", "download1.jpeg", "download2.jpeg", "download3.jpeg"],
                                   ".gif", "beautiful") == "Image successfully converted"
    with pytest.raises(SystemExit):
        convert_2_animated_gif("nature.gif", ["download1.jpeg", "download2.jpeg", "download3.jpeg"],
                                ".gif", "beautiful")
    with pytest.raises(SystemExit):
        convert_2_animated_gif(" bear.png", ["download1.jpeg", "download2.jpeg", "download3.jpeg"],
                                ".jpg", "beautiful")
