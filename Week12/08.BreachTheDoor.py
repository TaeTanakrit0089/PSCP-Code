'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    text = input().split()
    result = []
    for i in text:
        temp = 0
        text_temp = ''
        for j in i:
            if j.isalpha():
                temp += 1
                text_temp += j
        if temp > 6:
            result.append(text_temp)
    print(*result)


better_call_saul()
