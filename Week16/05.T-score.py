'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    num_n, num_m = int(input()), int(input())
    data = [int(input()) for _ in range(num_n)]
    data = [i for i in data if i <= num_m]
    avg = sum(data)/num_n
    std_dv = (((num_n * sum([i**2 for i in data])) - (sum(data)**2)) / (num_n*(num_n-1))) ** 0.5
    data = [50 + 10*((i-avg)/std_dv) for i in data]
    for i in data:
        print('%.2f' % round(i, 2))
better_call_saul()
