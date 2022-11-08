'''Saul Goodman'''


def huell():
    '''Saul Goodman'''
    days_one = [int(input()), int(input())]
    days_two = [int(input()), int(input())]

    temp1, temp2 = find_days(days_one), find_days(days_two)
    temp3 = abs(temp1-temp2)
    print(temp3)

def find_days(day):
    '''Saul Goodman'''
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sumdays = sum(days[:day[1]])
    return sumdays + day[0]


huell()
