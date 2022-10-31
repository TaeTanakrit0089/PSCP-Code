"""Pre"""


def blue_screen():
    """Pre"""
    num1 = int(input())
    lis = [["  " for i in range(num1)]for i in range(num1)]

    row = -1
    while True:
        row += 1
        if row == num1:
            break
        for i in range(row+1,0,-1):
            lis[row][-i] = i

    print(*lis, sep='\n')


blue_screen()
