'''Pre'''


def main():
    '''Pre'''
    num1 = int(input())
    num2 = int(input())
    people = input()

    if people == 'B':
        temp = num2
        num2 = num1
        num1 = temp
    result = (1) / (1 + 10**((num2-num1)/400))
    result = round(result, 2)
    print("%.2f" % result)


main()
