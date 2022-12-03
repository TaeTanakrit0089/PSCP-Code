"""Steve walks warily down the street"""
def another_one_bite_the_dust():
    """With his brim pulled way down low"""
    seat_per_row, column, ticket = int(input()), int(input()), int(input())
    temp1, temp2, temp3 = seat_per_row, seat_per_row*(column+1), 1
    for i in range(seat_per_row):
        for j in range(temp1, temp2, seat_per_row):
            print('%02d' % j if j != ticket else 'XX', end=' ')
        if i+1 == seat_per_row:
            break
        print('\n' if temp3 % 2 == 1 and i != seat_per_row else '\n\n', end='')
        temp1, temp2, temp3 = temp1 - 1, temp2 - 1, temp3 + 1

another_one_bite_the_dust()
