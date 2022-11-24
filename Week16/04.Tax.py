'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    year, engine, summer = int(input()), int(input()), 0
    if engine in range(601):
        summer = engine * 0.5
    elif engine in range(601, 1801):
        summer = 300 + (engine - 600) * 1.5
    else:
        summer = 2100 + (engine - 1800) * 4

    discount = {6: 10, 7: 20, 8: 30, 9: 40}
    if year in discount:
        summer *= (100 - discount[year])/100
    elif year >= 10:
        summer *= 0.5

    print('%.2f' % summer)


better_call_saul()
