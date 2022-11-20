'''Saul Goodman'''
def better_call_saul():
    '''Obama used to say that bubble sort is not the best method.'''
    temp, data, before = input(), [], []
    while temp != 'END':
        data.append(int(temp))
        temp = input()
    while before != data:
        before = data.copy()
        for i in range(len(data)-1):
            if data[i+1] < data[i]:
                data[i], data[i+1] = data[i+1], data[i]
    print(*data, sep='\n')

better_call_saul()
