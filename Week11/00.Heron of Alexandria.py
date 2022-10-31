'''prepro'''


def main():
    '''Prepro'''
    ip_a = float(input())
    ip_b = float(input())
    ip_c = float(input())

    num_s = (ip_a+ip_b+ip_c)/2

    area = (num_s*(num_s-ip_a)*(num_s-ip_b)*(num_s-ip_c))**0.5
    print('%.03f' % round(area, 3))


main()
