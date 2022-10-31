"""Pre"""


def blue_screen():
    """Pre"""
    lis = []
    num1 = int(input())
    for _ in range(1, num1+1):
        lis.append(_)
        print(*lis)

    for _ in range(1, num1):
        del lis[-1]
        print(*lis)


blue_screen()
