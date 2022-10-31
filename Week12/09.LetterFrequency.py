'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    text = input()
    text_no_space = dict.fromkeys(text.replace(' ', ''))
    for key, _ in text_no_space.items():
        text_no_space[key] = text.count(key)
    result = sorted(text_no_space.items(), key=lambda l: l[1], reverse=True)
    print(result[0][0])


better_call_saul()
