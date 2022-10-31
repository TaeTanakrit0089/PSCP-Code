'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    model = input()
    storage = input()

    storage = convert_unit(storage)

    if model == 'iPhone 13 mini':
        mini_model(storage)
    elif model == 'iPhone 13':
        standard_model(storage)
    elif model == 'iPhone 13 Pro':
        pro_model(storage)
    elif model == 'iPhone 13 Pro Max':
        pro_max_model(storage)
    else:
        print('Not Available')


def mini_model(storage):
    '''Saul Goodman'''
    if storage == 128:
        print(25900)
    elif storage == 256:
        print(29900)
    elif storage == 512:
        print(37900)
    else:
        print('Not Available')


def standard_model(storage):
    '''Saul Goodman'''
    if storage == 128:
        print(29900)
    elif storage == 256:
        print(33900)
    elif storage == 512:
        print(41900)
    else:
        print('Not Available')


def pro_model(storage):
    '''Saul Goodman'''
    if storage == 128:
        print(38900)
    elif storage == 256:
        print(42900)
    elif storage == 512:
        print(50900)
    elif storage == 1000:
        print(58900)
    else:
        print('Not Available')


def pro_max_model(storage):
    '''Saul Goodman'''
    if storage == 128:
        print(42900)
    elif storage == 256:
        print(46900)
    elif storage == 512:
        print(54900)
    elif storage == 1000:
        print(62900)
    else:
        print('Not Available')


def convert_unit(unit):
    '''Saul Goodman'''
    unit = unit.split()

    if unit[1] == 'TB':
        unit[0] = int(unit[0]) * 1000

    return int(unit[0])


main()
