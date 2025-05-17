#!/usr/bin/python3

def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    
    for letter in text:
        print(letter, end="")
        if letter in ".?:":
            print()
            print()