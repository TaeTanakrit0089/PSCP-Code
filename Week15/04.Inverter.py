'''Saul Goodman'''
def huell():
    '''Saul Goodman'''
    text, inverted = input(), ''
    for i in text:
        if i == '1':
            inverted += '0'
        else:
            inverted += '1'
    if int(inverted) == 0:
        return
    print(int(inverted))
huell()
