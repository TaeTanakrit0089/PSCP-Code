'''Python'''


def main():
    '''Python'''
    phone_num = input()
    carrier_info = input()

    result = domestic_call(phone_num)

    if carrier_info == 'International':
        result = international_call(result)

    print(result)


def domestic_call(phone_num):
    '''Python'''

    if len(phone_num) == 9:
        result = phone_num[0:1] + ' ' + phone_num[1:5] + ' ' + phone_num[5:]
    elif len(phone_num) == 10:
        result = phone_num[0:2] + ' ' + phone_num[2:6] + ' ' + phone_num[6:]

    return result


def international_call(phone_num):
    '''Python'''
    phone_num = '+66' + phone_num[1:]
    return phone_num


main()
