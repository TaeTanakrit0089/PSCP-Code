'''Saul Goodman'''


def goodman():
    '''Saul GOodman'''
    input1 = input()
    input2 = input()
    input3 = input()
    finger = int(input())
    eat = input2.count(')', 0, finger)
    input2 = ' '*finger + input2[finger:]
    left = input2.count(')')
    print(eat)
    if left > 0:
        print('There are still some left.')
    else:
        print('None.')
    print(input1)
    print(input2)
    print(input3)


goodman()
