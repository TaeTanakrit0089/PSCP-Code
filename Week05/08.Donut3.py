'''Mr.White'''


def breaking_bad():
    '''Mr.White'''
    price_per_piece = int(input())
    donut_amount = int(input())
    give_free = int(input())
    at_least = int(input())

    promo = at_least // (donut_amount + give_free)
    donut_left = at_least - promo*(donut_amount + give_free)

    if donut_left >= donut_amount:
        promo += 1
        cost = price_per_piece * donut_amount * promo
        donut = (donut_amount+give_free) * promo
    elif donut_left < donut_amount:
        cost = (price_per_piece * donut_amount * promo) + \
            price_per_piece*donut_left
        donut = ((donut_amount+give_free) * promo) + donut_left

    print(cost, donut)


breaking_bad()
