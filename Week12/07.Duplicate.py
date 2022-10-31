'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    num_n, num_m = int(input()), int(input())
    set_a = set([int(input()) for i in range(num_n)])
    set_b = set([int(input()) for i in range(num_m)])

    result = set()
    detected = False
    for i in set_a:
        if i in set_b:
            detected = True
            result.add(i)
    for i in set_b:
        if i in set_a and i not in result:
            detected = True
            result.add(i)
    result = sorted(result, reverse=True)
    if not detected:
        print('Nope')
    else:
        print(*result, sep='\n')


better_call_saul()
