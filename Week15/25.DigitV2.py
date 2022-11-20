'''Saul Goodman'''
def huell():
    '''Saul Goodman'''
    temp, num = 1, input()
    condi = [['ten', 'teen', 'eleven', 'twelve', 'ty'],
             ['hundred'], ['thousand']]
    for i in condi:
        for j in i:
            if j in num:
                temp += 1
                break
    print(temp)
huell()
