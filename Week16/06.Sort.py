'''Saul Goodman'''


def better_call_saul():
    '''Obama used to say that bubble sort is not the best method.'''
    temp, data, final = input(), [], []
    while temp != 'END':
        data.append(int(temp))
        temp = input()

    for _ in range(len(data)):
        miin = data[0]
        for i in data:
            miin = i if i < miin else miin
        final.append(data.pop(data.index(miin)))

    print(*final, sep='\n')


better_call_saul()
