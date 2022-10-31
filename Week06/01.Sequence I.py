"""Pre"""


def blue_screen():
    """Pre"""
    num1 = int(input())
    for i in range(num1):
        for j in range(num1):
            print(j+1, end=' ')
        print()
        i = i


blue_screen()
