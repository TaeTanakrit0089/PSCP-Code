'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    data = []
    cat_lost, fox_lost = False, False
    c_cat, c_fox = 0, 0
    for _ in range(int(input())):
        temp_in = input()
        temp1, temp2 = temp_in.split('"'), temp_in.split("'")
        if len(temp1) > len(temp2):
            temp_out = [temp1[1], temp1[3]]
        else:
            temp_out = [temp2[1], temp2[3]]
        data.append(
            {'Name': temp_out[0], 'Type': temp_out[1][:3], 'Number': int(temp_out[1][3:])})
    for i in data:
        if 'Cat' in i['Type']:
            c_cat += 1
        elif 'Fox' in i['Type']:
            c_fox += 1

        if i['Name'] == 'Garfield' or (i['Type'] == 'Cat' and i['Number'] == 1):
            cat_lost = True
        if i['Name'] == 'Fubuki' or (i['Type'] == 'Fox' and i['Number'] == 1):
            fox_lost = True
    if not cat_lost:
        data.append({'Name': 'Garfield', 'Type': 'Cat', 'Number': 1})
        c_cat += 1
    if not fox_lost:
        data.append({'Name': 'Fubuki', 'Type': 'Fox', 'Number': 1})
        c_fox += 1

    data.sort(key=goodman)

    print('Cat :', c_cat)
    print('Fox :', c_fox)
    for i in data:
        print('%s : %s%02d' % (i['Name'], i['Type'], i['Number']))


def goodman(gusfring):
    '''C: 43, 0: Missing function docstring (missing-docstring)'''
    if gusfring['Type'] == 'Cat':
        pollos = '1'
    else:
        pollos = '2'
    pollos += str('%020d' % gusfring['Number'])
    return pollos


better_call_saul()
