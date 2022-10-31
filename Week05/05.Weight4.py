"""Saul Goodman"""


def breaking_bad():
    '''Saul GOodman'''
    avg = float(input())
    weight1 = float(input())
    weight2 = float(input())
    weight3 = float(input())
    weight_lost = avg*4-weight1-weight2-weight3

    if overweight(avg) and unbalance(weight1, weight2, weight3, weight_lost, avg):
        print("Overweight")
    elif overweight(avg):
        print("Overweight")
    elif unbalance(weight1, weight2, weight3, weight_lost, avg):
        print("Unbalance")
    else:
        print("Pass %.2f" % weight_lost)


def overweight(avg):
    '''Saul Goodman'''
    return avg*4 > 15000


def unbalance(num1, num2, num3, num4, avg):
    '''Saul Goodman'''
    if abs(num1-avg) > avg/2 or abs(num2-avg) > avg/2 or\
            abs(num3-avg) > avg/2 or abs(num4-avg) > avg/2:
        return True
    return False


breaking_bad()
