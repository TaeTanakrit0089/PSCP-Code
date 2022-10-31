'''Having trouble with money laundering? Better Call Saul!!!'''

from math import floor


def tax_cheater():
    '''Being tax_cheater is million times worse than being a criminal'''
    income = float(input())
    sum_tax = 0
    sum_tax += cal_tax_firsthalf(income)
    sum_tax += cal_tax_secondhalf(income)

    print(floor(sum_tax))


def cal_tax_firsthalf(income):
    '''Saul Goodman! Justice for you!'''
    sum_tax = 0

    if income in range(0, 150000):
        return 0

    if income in range(150000, 300000):
        sum_tax += (income - 150000) * 5/100
        return sum_tax
    else:
        sum_tax += 150000 * 5/100

    if income in range(300000, 500000):
        sum_tax += (income - 300000) * 10/100
        return sum_tax
    else:
        sum_tax += 200000 * 10/100

    if income in range(500000, 750000):
        sum_tax += (income - 500000) * 15/100
        return sum_tax
    else:
        sum_tax += 250000 * 15/100

    return sum_tax


def cal_tax_secondhalf(income):
    '''Saul Goodman! Justice for you!'''
    sum_tax = 0

    if income in range(0, 750000):
        return 0

    if income in range(750000, 1000000):
        sum_tax += (income - 750000) * 20/100
        return sum_tax
    else:
        sum_tax += 250000 * 20/100

    if income in range(1000000, 2000000):
        sum_tax += (income - 1000000) * 25/100
        return sum_tax
    else:
        sum_tax += 1000000 * 25/100

    if income in range(2000000, 4000000):
        sum_tax += (income - 2000000) * 30/100
        return sum_tax
    else:
        sum_tax += 2000000 * 30/100

    if income >= 4000000:
        sum_tax += (income - 4000000) * 35/100
        return sum_tax

    return sum_tax


tax_cheater()
