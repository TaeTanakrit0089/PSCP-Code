'''Mr.White'''


def breaking_bad():
    '''Mr.White'''
    price_per_piece = int(input())
    donut_amount = int(input())
    give_free = int(input())
    at_least = int(input())

    temp = 1
    summer = 0
    while summer < at_least:
        summer = find_sum(donut_amount, give_free, temp)
        if summer >= at_least:
            break
        temp += 1

    amount_to_pay = (price_per_piece*donut_amount*temp)
    amount_donut = temp*(donut_amount+give_free)
    print("Temp =",temp)
    print(amount_to_pay, amount_donut)


def find_sum(num1, num2, times):
    '''Mr.Goodman'''
    return (num1*times) + (num2*times)


breaking_bad()
