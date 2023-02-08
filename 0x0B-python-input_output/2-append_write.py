#!/usr/bin/python3
def append_write(filename="", text=""):
    """function to append a text to a file """
    with open(filename, 'a', encoding='UTF8') as f:
        print(f.write(text))
