'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    result = ''
    first_chr = True
    before_temp = 0
    while True:
        temp = int(input())

        if first_chr:
            first_num = temp
            first_chr = False
            if temp == -1:
                break
            before_temp = temp
            continue

        if temp == -1:
            if first_num == before_temp:
                result += ('%d' % first_num)
            else:
                result += ('%d-%d' % (first_num, before_temp))
            break
        elif temp - before_temp == 1:
            before_temp = temp
            continue
        else:
            if first_num == before_temp:
                result += ('%d, ' % first_num)
            else:
                result += ('%d-%d, ' % (first_num, before_temp))

        first_num, before_temp = temp, temp

    if result == '':
        return 0
    print(result)


main()
