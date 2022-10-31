'''prepro'''


def main():
    '''Prepro'''
    percan = int(input())
    cap = int(input())
    discount = int(input())
    want = int(input())

    result = 0
    count = 0

    if cap == 0:
        print(percan*want)
        return 0

    for _ in range(1, want+1):
        if count == cap:
            result += discount
            count = 0
        else:
            result += percan
        count += 1
    print(result)


main()
