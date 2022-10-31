'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    text_input = input()
    text_pair = []
    temp = '0'
    for i in text_input:
        if i.isalpha():
            text_pair.append([int(temp[1:]), i])
            temp = '0'
            continue
        temp += i

    for i in text_pair:
        print(i[1]*int(i[0]), end='')
    print()


better_call_saul()
