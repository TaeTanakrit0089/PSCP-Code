"""Python"""


def main():
    """Python"""
    get_point = 0
    have_a = False
    num_card = int(input())
    for i in range(num_card):
        text_input = input()
        if text_input == 'A':
            have_a = True
        get_point = cal_point(text_input, get_point)
        i = i

    if have_a == True and get_point > 21:
        get_point -= 10
    print(get_point)


def cal_point(card, point):
    '''card'''
    if card == 'J' or card == 'Q' or card == 'K':
        point += 10
    elif card.isnumeric():
        point += int(card)
    else:
        if point > 10:
            point += 1
        else:
            point += 11

    return point


main()
