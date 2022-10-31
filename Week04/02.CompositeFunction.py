'''Python'''


def main():
    '''Python'''
    num1 = float(input())
    first_row = func_f(func_g(num1))
    second_row = func_g(func_f(num1))
    print("%.2f" % first_row)
    print("%.2f" % second_row)


def func_f(num1):
    """ppp"""
    num2 = 2*num1
    return num2


def func_g(num1):
    """ppp"""
    num2 = num1/2 + 1
    return num2


main()
