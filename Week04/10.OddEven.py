'''Pre'''


def main():
    '''Pre'''
    num_1 = int(input())
    if is_odd(num_1):
        print("True")
    else:
        print("False")

def is_odd(num1):
    '''ppp'''
    if num1 % 2 == 1:
        return True
    else:
        return False

main()
