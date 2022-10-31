"""Pre"""


def blue_screen():
    """Pre"""
    num1 = int(input())
    temp = 1
    while True:
        if temp == num1**2:
            print(temp)
            break
        if temp % num1 == 0:
            print(temp)
            temp += 1
            continue
        print(temp, end=' ')
        temp += 1


blue_screen()
