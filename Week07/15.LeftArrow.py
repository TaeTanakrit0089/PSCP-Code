'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num_a = int(input())
    num_b = int(input())
    space_row = (num_b//2)
    for i in range(space_row, -1, -1):
        print(" "*i, end='')
        print("*"*num_a, end='')
        print()

    for i in range(1, space_row+1):
        print(" "*i, end='')
        print("*"*num_a, end='')
        print()


main()
