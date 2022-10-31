'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def yes_or_no(text):
    '''Saul Goodman'''
    if text == 'Yes':
        return True
    return False


def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    screens, phones = int(input()), int(input())
    input(), input()
    on_tv = yes_or_no(input())
    fhd, uhd = yes_or_no(input()), yes_or_no(input())

    c_mobile, c_basic, c_standard, c_premium, price = 0, 0, 0, 0, 0
    while screens or phones:
        if (on_tv or fhd or uhd) and (screens >= 3 or phones >= 3) or fhd:
            price += 419
            c_premium += 1
            screens -= 4
            phones -= 4
        elif (fhd or on_tv) and (screens >= 2 or phones >= 2) or fhd:
            price += 349
            c_standard += 1
            screens -= 2
            phones -= 2
        elif on_tv and not fhd and not uhd and (screens >= 1 or phones >= 1):
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

    if c_premium:
        print("Premium x", c_premium)
    if c_standard:
        print("Standard x", c_standard)
    if c_basic:
        print("Basic x", c_basic)
    if c_mobile:
        print("Mobile x", c_mobile)
    print('Total = %d THB' % price)


better_call_saul()
