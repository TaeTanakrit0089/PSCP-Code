'''prepro'''


def main():
    '''Prepro'''
    num = [int(input()) for i in range(5)]
    num.sort()
    print(*num, sep='\n')


main()
