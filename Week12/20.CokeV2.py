'''OH! I'm wanna drink some soda!!!'''
def better_drink_coke(percan, cap, dispercan, atleast):
    '''Better Call Cola-Cola'''
    if cap <= 0:
        return percan * atleast
    if atleast == 0:
        return 0
    atleast -= 1
    promo_range = (percan*(cap-1)) + dispercan
    possible_promo, can_left = atleast // cap, atleast % cap
    return percan + (promo_range * possible_promo) + (percan * can_left)
print('%d' %better_drink_coke(float(input()), int(input()), float(input()), int(input())))

