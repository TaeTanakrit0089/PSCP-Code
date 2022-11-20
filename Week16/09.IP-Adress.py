'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    text = input()
    temp = text.replace(' ', '').replace('\t', '')
    temp = ''.join(c for c in temp if c.isdigit() or c == '.')
    condi1 = text.count('.') != 3 or text != temp
    temp = temp.split('.')
    if not condi1:
        for i in temp:
            if int(i) not in range(0, 256):
                condi1 = True
    if condi1:
        print('Invalid IPv4 address')
    else:
        print(*list(map(int, temp)), sep='.')

better_call_saul()
