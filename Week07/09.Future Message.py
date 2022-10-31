'''Marty Mcfly'''


def future():
    '''Marty Mcfly'''
    text = input()
    if text.istitle():
        print("Title")
    elif text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.isspace():
        print("Space")
    elif text.isnumeric():
        print("Number")
    else:
        print("Other")


future()
