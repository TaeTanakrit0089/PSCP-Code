'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    data = do_text_thing()
    cat_num, fox_num = 0, 0
    for key, values in data.items():
        if 'Cat' in key:
            cat_num += 1
        elif 'Fox' in key:
            fox_num += 1
    print('Cat : %d' % cat_num)
    print('Fox : %d' % fox_num)
    for key, values in data.items():
        print(values, ":", key)


def do_text_thing():
    '''Saul Goodman'''
    num_1 = int(input())
    data = {}
    for i in range(num_1):
        error = ['"', "'", ',', ':']
        temp1 = input()
        temp2, stat = ['' , ''], 0
        for i in temp1:
            if i.isalpha() or i.isalnum():
                temp2[stat] += i
            if len(temp2[0]) > 0 and i in error:
                stat = 1
        data.update({temp2[0]: temp2[1]})
    if 'Cat01' not in data.values() and 'Garfield' not in data:
        data.update({"Garfield": "Cat01"})
    if 'Fox01' not in data.values() and 'Fubuki' not in data:
        data.update({"Fubuki": "Fox01"})
    new_data = [[value, key] for key, value in data.items()]
    new_data.sort(key=split_num)
    return dict(new_data)


def split_num(text1):
    '''Saul Goodman'''
    print(text1[0][-2:])
    return text1[0][-2:]


better_call_saul()
