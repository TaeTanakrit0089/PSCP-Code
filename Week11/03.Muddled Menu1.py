'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    menu = do_menu_thing()
    if menu == 0:
        return 0
    full_course, result = [], ''
    for key, _ in menu.items():
        full_course.append(key)
    result += 'Full Course: ' + str(full_course)
    full_course.reverse()
    result += ' Reversed: ' + str(full_course)
    print(result)


def do_menu_thing():
    '''Saul Goodman'''
    goodman = input()
    all_menu, cannot_do = [], []
    while goodman != 'DONE':
        if goodman == 'CLOSED':
            print('Full Course: [] Reversed: []')
            return 0
        elif "Can't do: " in goodman:
            cannot_do += goodman.replace("Can't do: ", '').split(', ')
        elif goodman == "SOMETHING'S WRONG":
            all_menu = []
        else:
            all_menu.append(goodman.split(' #'))
        goodman = input()
    menu = dict(all_menu)
    for i in cannot_do:
        del menu[i]
    menu = sorted(menu.items(), key=lambda l: l[0])
    menu = sorted(menu, key=lambda l: l[1])
    return dict(menu)


better_call_saul()
