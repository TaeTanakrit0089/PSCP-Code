"""Steve walks warily down the street"""
def another_one_bite_the_dust():
    """With his brim pulled way down low"""
    cost_per_left = float(input())
    cap = int(input())
    reward = int(input())
    every = int(input())
    more = int(input())
    money = float(input())

    buy = money // cost_per_left
    milk = all_covers = left = buy
    while all_covers >= cap or left >= every:
        temp1 = (all_covers // cap) * reward
        temp2 = temp1 + (left // every) * more
        all_covers = temp2 + all_covers % cap
        left = temp2 + left % every
        milk += temp2
    print('%d' % milk)
another_one_bite_the_dust()
