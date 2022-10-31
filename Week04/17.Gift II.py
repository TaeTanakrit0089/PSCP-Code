'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    result = 0
    result = check(int(input()), result)
    result = check(int(input()), result)
    result = check(int(input()), result)
    result = check(int(input()), result)
    result = check(int(input()), result)
    result = check(int(input()), result)
    result = check(int(input()), result)
    result = check(int(input()), result)
    print(result)


def check(num1, num2):
    '''Saul Goodman'''
    if num1 % 2 == 0:
        return num1
    return num2


main()
