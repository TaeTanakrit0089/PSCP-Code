'''Mr.White'''


def breaking_bad():
    '''Mr.White'''
    price_per_piece = int(input())
    donut_amount = int(input())
    give_free = int(input())
    at_least = int(input())

    if donut_amount == at_least:
        temp = at_least // donut_amount
    elif at_least < donut_amount:
        print(at_least*price_per_piece, at_least)
        return 0
    elif at_least % (donut_amount+give_free) == 0:
        temp = at_least // (donut_amount + give_free)
    else:
        temp = (at_least // (donut_amount + give_free)) + 1

    amount_to_pay = price_per_piece*donut_amount*temp
    amount_donut = temp*(donut_amount+give_free)
    print(amount_to_pay, amount_donut)


breaking_bad()
