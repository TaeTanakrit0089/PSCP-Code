'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    mac = input().upper()
    all_error = False
    rmac = ''
    pat1, pat2, pat3 = '', '', ''
    for i in mac:
        i = i.upper()
        if i.isalpha() or i.isnumeric():
            rmac += i
        condi1 = ord(i) not in range(65, 71) and i.isalpha()
        if condi1:
            all_error = True

    if len(rmac) != 12 or all_error:
        print('ERROR')
        return 0

    # pattern1
    for i in range(0, 12, 2):
        pat1 += rmac[i]+rmac[i+1]+'-'
    pat1 = pat1[:-1]

    # pattern2
    for i in range(0, 12, 2):
        pat2 += rmac[i]+rmac[i+1]+':'
    pat2 = pat2[:-1]

    # pattern3
    for i in range(0, 12, 4):
        pat3 += rmac[i]+rmac[i+1]+rmac[i+2]+rmac[i+3]+'.'
    pat3 = pat3[:-1]

    if mac == pat1:
        print('VALID 1')
    elif mac == pat2:
        print('VALID 2')
    elif mac == pat3:
        print('VALID 3')
    else:
        print('ERROR')


main()
