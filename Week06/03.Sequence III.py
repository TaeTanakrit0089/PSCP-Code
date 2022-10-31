"""Pre"""


def blue_screen():
    """Pre"""
    num1 = int(input())
    for i in range(2, num1+2):
        plus = 0
        for _ in range(num1):
            cal = i+plus
            print(cal, end=' ')
            plus += 1
        print()


blue_screen()
