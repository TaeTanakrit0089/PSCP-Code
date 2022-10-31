'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    first_prize = input()
    last_two_digit = input()
    first_three_digit_one, first_three_digit_two = input(), input()
    last_three_digit_one, last_three_digit_two = input(), input()
    my_lottery = input()

    sum_all = 0
    # firstprize
    if first_prize == my_lottery:
        sum_all += 6000000

    # last two
    if my_lottery[-2:] == last_two_digit:
        sum_all += 2000

    # three digit
    condi31 = my_lottery[:3] == first_three_digit_one
    condi32 = my_lottery[:3] == first_three_digit_two
    condi33 = my_lottery[-3:] == last_three_digit_one
    condi34 = my_lottery[-3:] == last_three_digit_two

    if condi31:
        sum_all += 4000
    if condi32:
        sum_all += 4000
    if condi33:
        sum_all += 4000
    if condi34:
        sum_all += 4000

    # near first prize
    condi1 = nearly_reward(my_lottery, first_prize)
    if condi1:
        sum_all += 100000
    print(sum_all)


def nearly_reward(my_lotto, firstreward):
    '''Saul Goodman'''

    condi1 = my_lotto == '999999' and firstreward == '000000'
    condi2 = my_lotto == '000000' and firstreward == '999999'
    my_lotto, firstreward = int(my_lotto), int(firstreward)
    condi3 = abs(my_lotto-firstreward) == 1

    if condi1 or condi2 or condi3:
        return True
    return False


main()
