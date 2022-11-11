'''Saul Goodman'''


def huell():
    '''Saul Goodman'''
    temp, data, canbe, notbe = input(), [], set(), set()
    result = set([i for i in range(101)])
    while temp != 'END':
        text = temp.split()
        data.append([text[0], int(text[1]), text[2]])
        temp = input()
    for i in data:
        if i[0] == '>':
            temp = [i for i in range(i[1]+1, 101)]
        elif i[0] == '<':
            temp = [i for i in range(0, i[1])]
        else:
            temp = [i[1]]

        if i[2] == 'YES':
            canbe.update(set(temp))
        else:
            notbe.update(set(temp))
    
    result = result - notbe 
    result = result.intersection(canbe)
    print(*result)


huell()
