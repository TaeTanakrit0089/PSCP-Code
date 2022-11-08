'''Saul Goodman'''
 
 
def huell():
    '''Saul Goodman'''
    temp, data, all_possible, restrict = input(), [], [], []
    while temp != 'END':
        data.append(temp.split())
        temp = input()
    data = [[i[0], int(i[1]), define_bool(i[2])] for i in data]
    data.sort(key=lambda l: l[2], reverse=1)
    for i in data:
        if i[2]:
            if i[0] == '>':
                all_possible.append(set(i for i in range(i[1]+1, 101)))
            elif i[0] == '<':
                all_possible.append(set(i for i in range(0, i[1])))
            else:
                all_possible.append(set([i[1]]))
        elif not i[2]:
            if i[0] == '>':
                restrict += [i for i in range(i[1]+1, 101)]
            elif i[0] == '<':
                restrict += [i for i in range(0, i[1])]
            else:
                restrict.append(i[1])
 
    final_data = set(i for i in range(0, 101))
    for i in list(dict.fromkeys(restrict)):
        final_data.remove(i)
    final_data = final_data.intersection(*all_possible)
 
    print(*final_data)
 
 
def define_bool(text):
    if text == 'YES':
        return True
    return False
 
 
huell()