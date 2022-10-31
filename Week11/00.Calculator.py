'''prepro'''


def main():
    '''Prepro'''
    num = int(input())
    count = 0

    if num == 1:
        print(1)
        return 0

    for i in range(1, num+1):
        count += len(str(i))+1
    print(count)


main()
