'''Saul Goodman'''


def amicable_formula(num):
    '''Saul Goodman'''
    num_p = 3 * (2**(num-1)) - 1
    num_q = 3 * (2**(num)) - 1
    num_r = 9 * (2**(2*num-1)) - 1
    first, second = 2**num * num_p * num_q, 2**num * num_r
    return [first, second]


def better_call_saul():
    '''Saul Goodman'''
    goodman = int(input())
    ami, temp, summer = [0], 2, 0
    print(amicable_formula(goodman))
    return
    while ami[-1] < goodman:
        ami += amicable_formula(temp)
        temp += 1
    for i in sorted(ami):
        if i > goodman:
            break
        summer += i
    print(ami)


better_call_saul()
