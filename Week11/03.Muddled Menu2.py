'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    data = do_text_thing()
    menu_name = list(data)
    print('Full Course:', menu_name, end=' ')
    print('Reversed:', menu_name[::-1])


def do_text_thing():
    '''Saul Goodman'''
    temp = input()
    all_data, data_rm = [], []
    while temp != 'DONE':
        if temp == 'CLOSED':
            return {}
        elif "Can't do: " in temp:
            data_rm.append(temp.replace("Can't do: ", ''))
        elif temp == "SOMETHING'S WRONG":
            all_data = []
        else:
            all_data.append(temp.split(' #'))
        temp = input()
    data = dict(all_data)
    for i in data_rm:
        del data[i]
    data = dict(sorted(data.items(), key=lambda l: l[0]))
    return dict(sorted(data.items(), key=lambda l: l[1]))

better_call_saul()
