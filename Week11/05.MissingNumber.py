'''prepro'''


def main():
    '''Prepro'''
    num = []
    first_num = int(input())
    temp = int(input())
    while temp != 0:
        num.append(temp)
        temp = int(input())
    num.sort()
    num = list(dict.fromkeys(num))

    for i in range(1, first_num+1):
        if i not in num:
            print(i)


main()
