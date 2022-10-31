"""Pre"""


def blue_screen():
    """Pre"""
    num1 = int(input())
    temp = num1
    num_per_row = 0
    while True:
        num_per_row += 1
        if temp == 1:
            print(temp)
            break
        if num_per_row == 7:
            print(temp)
            num_per_row = 0
            temp -= 1
            continue
        print(temp, end=' ')
        temp -= 1


blue_screen()
