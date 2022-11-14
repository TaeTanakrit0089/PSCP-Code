'''Saul Goodman'''


def huell():
    '''Saul Goodman'''
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    all_days = [[int(input()), int(input())] for _ in range(2)]
    all_days.sort(key=lambda l: l[1])
    days_one, days_two = all_days[0], all_days[1]

    condi1 = days_one[0] > days[days_one[1] -
                                1] or days_two[0] > days[days_two[1]-1]
    if condi1:
        return "Impossible"
    count = 0
    while days_one != days_two:
        days_one[0] += 1
        if days_one[0] > days[days_one[1]-1]:
            days_one[0] = 1
            days_one[1] += 1
            if days_one[1] > 12:
                days_one[1] = 1
        count += 1
    return count


print(huell())
