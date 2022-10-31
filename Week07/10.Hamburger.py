'''BurgerKing'''


def whopper():
    '''Burgerking'''
    num1 = int(input())
    num2 = int(input())
    print("|"*num1, end='')
    print("*"*((num1+num2)*2), end='')
    print("|"*num2, end='')
    print()


whopper()
