import requests

def text_to_handwriting(string: str, save_to: str = "text.png", rgb: list = [0, 0, 138]) -> None:
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
    file = open(save_to, "wb")
    file.write(data)
    file.close()

text_to_handwriting("Hi", rgb=(0,0,225))

import requests


def text_to_handwriting(string: str, save_to: str = "a.png", rgb: tuple = (0, 0, 138)) -> None:
    """Convert the given str to handwriting"""
    data = requests.get(
        "https://pywhatkit.herokuapp.com/handwriting?text=%s&rgb=%s,%s,%s" % (string, rgb[0], rgb[1], rgb[2])).content
    with open(save_to, "wb") as file:
        file.write(data)
        file.close()

text_to_handwriting("text",rgb=[0,0,0])
