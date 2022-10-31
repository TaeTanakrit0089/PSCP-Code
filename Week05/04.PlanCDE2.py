'''pre'''


def main():
    '''pre'''
    stat = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    if stat == "Descend":
        if num1 >= num2 >= num3:
            print("%.2f, %.2f, %.2f" % (num1, num2, num3))
        elif num1 >= num3 >= num2:
            print("%.2f, %.2f, %.2f" % (num1, num3, num2))
        elif num2 >= num3 >= num1:
            print("%.2f, %.2f, %.2f" % (num2, num3, num1))
        elif num2 >= num1 >= num3:
            print("%.2f, %.2f, %.2f" % (num2, num1, num3))
        elif num3 >= num2 >= num1:
            print("%.2f, %.2f, %.2f" % (num3, num2, num1))
        elif num3 >= num1 >= num2:
            print("%.2f, %.2f, %.2f" % (num3, num1, num2))

    elif stat == "Ascend":
        asc(num1, num2, num3)


def asc(num1, num2, num3):
    '''Pre'''
    if num1 <= num2 <= num3:
        print("%.2f, %.2f, %.2f" % (num1, num2, num3))
    elif num1 <= num3 <= num2:
        print("%.2f, %.2f, %.2f" % (num1, num3, num2))
    elif num2 <= num3 <= num1:
        print("%.2f, %.2f, %.2f" % (num2, num3, num1))
    elif num2 <= num1 <= num3:
        print("%.2f, %.2f, %.2f" % (num2, num1, num3))
    elif num3 <= num2 <= num1:
        print("%.2f, %.2f, %.2f" % (num3, num2, num1))
    elif num3 <= num1 <= num2:
        print("%.2f, %.2f, %.2f" % (num3, num1, num2))


main()
