'''pre'''


def main():
    '''pre'''
    stat = input()
    num = [float(input()), float(input()), float(input())]

    if stat == "Descend":
        if num[0] >= num[1] >= num[2]:
            print("%.2f, %.2f, %.2f" % (num[0], num[1], num[2]))
        elif num[0] >= num[2] >= num[1]:
            print("%.2f, %.2f, %.2f" % (num[0], num[2], num[1]))
        elif num[1] >= num[2] >= num[0]:
            print("%.2f, %.2f, %.2f" % (num[1], num[2], num[0]))
        elif num[1] >= num[0] >= num[2]:
            print("%.2f, %.2f, %.2f" % (num[1], num[0], num[2]))
        elif num[2] >= num[1] >= num[0]:
            print("%.2f, %.2f, %.2f" % (num[2], num[1], num[0]))
        elif num[2] >= num[0] >= num[1]:
            print("%.2f, %.2f, %.2f" % (num[2], num[0], num[1]))

    elif stat == "Ascend":
        asc(num)


def asc(num):
    '''Pre'''
    if num[0] <= num[1] <= num[2]:
        print("%.2f, %.2f, %.2f" % (num[0], num[1], num[2]))
    elif num[0] <= num[2] <= num[1]:
        print("%.2f, %.2f, %.2f" % (num[0], num[2], num[1]))
    elif num[1] <= num[2] <= num[0]:
        print("%.2f, %.2f, %.2f" % (num[1], num[2], num[0]))
    elif num[1] <= num[0] <= num[2]:
        print("%.2f, %.2f, %.2f" % (num[1], num[0], num[2]))
    elif num[2] <= num[1] <= num[0]:
        print("%.2f, %.2f, %.2f" % (num[2], num[1], num[0]))
    elif num[2] <= num[0] <= num[1]:
        print("%.2f, %.2f, %.2f" % (num[2], num[0], num[1]))


main()
