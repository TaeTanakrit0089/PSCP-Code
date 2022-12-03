'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    text = input()
    alpha, temp, back_text = 'aeiouAEIOU', 0, ''
    for i in text[::-1]:
        temp -= 1
        if i in alpha:
            print(text[:temp], i*4, back_text[::-1], sep='')
            return
        else:
            back_text += i
    print(text)

better_call_saul()
