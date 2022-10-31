'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    num_all = int(input())
    if num_all == 0:
        return 0
    data, new_data = {}, {}
    for i in range(num_all):
        temp1, temp2 = input().split(':'), ['', '']
        count = 0
        for i in temp1:
            for j in i:
                if j.isnumeric() or j.isalpha():
                    temp2[count] += j
            data.update({temp2[0]: temp2[1]})
            count += 1
    if 'Cat01' not in data.values() and 'Garfield' not in data:
        data.update({"Garfield": "Cat01"})
    if 'Fox01' not in data.values() and 'Fubuki' not in data:
        data.update({"Fubuki": "Fox01"})
    new_data = dict(sorted([(value, key) for key, value in data.items()],key=lambda l:l[0]))
    all_cat, all_fox, result = 0, 0, [[], []]
    for key, values in new_data.items():
        if 'Cat' in key:
            all_cat += 1
            result[0].append('%s : %s' % (values, key))
        if 'Fox' in key:
            all_fox += 1
            result[1].append('%s : %s' % (values, key))
    print('Cat : %d' % all_cat)
    print('Fox : %d' % all_fox)
    for i in result:
        print(*i, sep='\n')


better_call_saul()
