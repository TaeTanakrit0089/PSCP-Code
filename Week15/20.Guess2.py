'''Saul Goodman'''


def huell():
    '''Saul Goodman'''
    temp, data, canbe, cannot = input(), [], [], []
    while temp != 'END':
        temp = temp.split()
        data.append([temp[0], int(temp[1]), temp[2]])
        temp = input()
    for i in data:
        if i[2] == 'YES':
            if i[0] == '>':
                temp = [i for i in range(i[1], 101)]
    final_data = set(i for i in range(0, 101))

    print(*final_data)


huell()
