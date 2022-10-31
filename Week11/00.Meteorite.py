'''prepro'''


def main():
    '''Prepro'''
    ip_a = float(input())
    ip_b = float(input())
    ip_c = float(input())
    ip_n, result = 0, 0

    while ip_a >= ip_c:
        result += ip_b**ip_n
        ip_n += 1
        ip_a = ip_a/ip_b

    print(int(result))


main()
