'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num_input = int(input())
    if num_input == 0:
        return 0
    all_name = ''
    for i in range(num_input):
        name_input = input()
        if i % 2 == 0:
            symbol = '-'
        else:
            symbol = '*'

        all_name += symbol*i + name_input

    print('%s_%d' % (all_name, num_input))


main()
