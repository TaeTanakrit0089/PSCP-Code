'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    kaprekar = input()
    sum_all = 0
    while kaprekar != 6174:
        kaprekar = arrange_num(str(kaprekar))
        sum_all += 1

    print(sum_all)


def set_zero(num1):
    '''Saul Goodman'''
    len_num = len(num1)
    if len_num < 4:
        zero_needed = 4 - len_num
        num1 = '0'*zero_needed + num1
    return num1


def arrange_num(num1):
    ''''I Better Call Saul'''
    smallest = int(num1)
    largest = int(num1)

    num1 = set_zero(num1)

    for numa in range(4):
        for numb in range(4):
            if numb == numa:
                continue
            for numc in range(4):
                if numc == numa or numc == numb:
                    continue
                for numd in range(4):
                    if numd == numc or numd == numb or numd == numa:
                        continue
                    num_a = num1[numa]
                    num_b = num1[numb]
                    num_c = num1[numc]
                    num_d = num1[numd]
                    num_all = int(num_a+num_b+num_c+num_d)
                    condi1 = num_all < smallest
                    condi2 = num_all > largest
                    if condi1:
                        smallest = num_all
                    elif condi2:
                        largest = num_all
    num_cal = largest - smallest
    #print('num1',largest, smallest ,num_cal)
    return num_cal


main()
