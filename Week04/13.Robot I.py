'''Pre'''


def main():
    '''Pre'''
    name = input()
    agee = float(input())
    if agee < 18:
        print(name, ", you can pass.", sep='')
    else:
        print(name, ", you shall not pass.", sep='')


main()
