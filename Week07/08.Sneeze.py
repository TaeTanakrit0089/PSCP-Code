'''Marty Mcfly'''

from curses.ascii import isalnum


def future():
    '''Marty Mcfly'''
    text = input()
    if text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.istitle():
        print("Title")
    elif text.isspace():
        print("Space")
    elif text.isalnum():
        print("Number")
    else:
        print("Other")


future()
