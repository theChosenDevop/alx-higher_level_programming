#!/usr/bin/python3
""" defines append_write function """


def append_write(filename="", text=""):
    """
        filename: file to be write and append into
        text: source of text input to filename
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
