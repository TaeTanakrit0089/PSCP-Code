'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def yes_or_no(text):
    '''Saul Goodman'''
    if text.lower() == 'yes':
        return True
    return False


def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    screens, phones = int(input()), int(input())
    input()
    input()
    on_tv, fhd, uhd = yes_or_no(input()), yes_or_no(
        input()), yes_or_no(input())

    c_mobile, c_basic, c_standard, c_premium, price = 0, 0, 0, 0, 0
    while screens > 0 or phones > 0:
        if (on_tv or fhd or uhd) and (screens >= 3 or phones >= 3):
            price += 419
            c_premium += 1
            screens -= 4
            phones -= 4
        elif (fhd or on_tv) and (screens >= 2 or phones >= 2):
            price += 349
            c_standard += 1
            screens -= 2
            phones -= 2
        elif on_tv and not fhd and not uhd:
            price += 279
            c_basic += 1
            screens -= 1
            phones -= 1
        else:
            if uhd:
                price += 419
                c_premium += 1
                screens -= 4
                phones -= 4
            elif fhd:
                price += 349
                c_standard += 1
                screens -= 2
                phones -= 2
            elif on_tv:
                price += 279
                c_basic += 1
                screens -= 1
                phones -= 1
            else:
                price += 99
                c_mobile += 1
                screens -= 1
                phones -= 1

    if c_premium > 0:
        print("Premium x", c_premium)
    if c_standard > 0:
        print("Standard x", c_standard)
    if c_basic > 0:
        print("Basic x", c_basic)
    if c_mobile > 0:
        print("Mobile x", c_mobile)
    print('Total = %d THB' % price)


better_call_saul()
