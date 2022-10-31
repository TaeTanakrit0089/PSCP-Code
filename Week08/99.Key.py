'''Key'''


def main():
    '''Key
    '1234567890123'
     0123456789101112

    x[0] = '1'
    x[2] = '3'
    x[-1] = '3'
    x[-2] = '2'
    x[-3] = '1'

    x[start:stop:interval]
    x[1::] = '234567890123'
    x[3::] = '4567890123'
    x[1::2] = '246802'

    '''
    id_card = input()

    # condition1
    sum_all = 0
    for i in id_card:
        sum_all += int(i)

    # condition2
    last_word = int(id_card[-3::]) * 10

    # condition3
    last_num = str(last_word + sum_all)

    if len(last_num) > 4:
        print(last_num[-4::])
    elif int(last_num) < 1000:
        print(int(last_num) + 1000)
    else:
        print(last_num)


main()
