#!/usr/bin/python3
def append_write(filename="", text=""):
    """function to append a text to a file
        arg: filename- name of the file
            text- the text to 
    """
    with open(filename, 'a', encoding='UTF8') as f:
        """open the file in append mode"""
        print(f.write(text))
