'''Pre'''


def main():
    '''Pre'''
    num_x = float(input())
    num_y = float(input())
    if num_x == 0 and num_y == 0:
        print("O")
    elif num_y == 0:
        print("X")
    elif num_x == 0:
        print("Y")

    elif is_less(num_x) == False and is_less(num_y) == False:
        print("Q1")
    elif is_less(num_x) == True and is_less(num_y) == False:
        print("Q2")
    elif is_less(num_x) == True and is_less(num_y) == True:
        print("Q3")
    elif is_less(num_x) == False and is_less(num_y) == True:
        print("Q4")


def is_less(num1):
    '''ppp'''
    if num1 < 0:
        return True
    else:
        return False


main()
