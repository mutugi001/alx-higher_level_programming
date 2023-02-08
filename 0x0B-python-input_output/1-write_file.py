#!/usr/bin/python3
def write_file(filename="", text=""):
    """function/method to write to a file and create if file does not exist """
    with open(filename, 'w', encoding='UTF8') as f:
        print(f.write(text))
