'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num1 = input()
    num2 = input()
    num3 = input()

    met = [num1, num2, num3]
    x = met[find_max(int(num1), int(num2), int(num3))]
    print(x)

def find_max(num1,num2,num3):
    x1 = str(num1)
    x2 = str(num2)
    x3 = str(num3)
    if num1 > num2 and num1 > num3:
        if x1 > x2:
            return 0
        elif x2 > x3:
            return 1
    elif num2 > num1 and num2 > num3:
        return 1
    elif num3 > num2 and num3 > num1:
        return 2
    


main()
