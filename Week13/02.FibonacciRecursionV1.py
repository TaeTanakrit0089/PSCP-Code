'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def fibonacci(number):
    '''The Constitution says you do, and so do I.'''
    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(int(input())))
