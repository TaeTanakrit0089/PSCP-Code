'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    all_price = float(input())
    least_price = float(input())
    discount = float(input())
    offer = float(input())

    with_offer = all_price + offer
    condi1 = all_price + offer >= least_price
    if condi1:
        with_offer = with_offer * (100-discount)/100

    no_offer = all_price
    condi2 = all_price >= least_price
    if condi2:
        no_offer = no_offer * (100-discount)/100

    different = abs(with_offer-no_offer)
    condi1 = with_offer < no_offer
    condi2 = with_offer > no_offer

    if condi1:
        print('Yes %.3f' % different)
    elif condi2:
        print('No %.3f' % different)
    else:
        print('Yes')


main()
