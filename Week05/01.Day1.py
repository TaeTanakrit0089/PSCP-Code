'''ppp'''


def main():
    '''pre'''
    num1 = int(input())
    if num1 % 400 == 0 and num1 % 100 == 0:
        print("Yes")
    elif num1 % 4 == 0 and not num1 % 100 == 0:
        print("Yes")
    else:
        print("No")


main()
