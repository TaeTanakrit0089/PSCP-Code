'''Saul Goodman'''

def better_call_saul():
    '''Saul Goodman'''
    months, norm_price, extra_num = int(input()), float(input()), float(input())
    extra_price, limit = float(input()), float(input())
    data, summer = [float(input()) for _ in range(months)], 0

    for i in data:
        temp1 = min(extra_num, i) * norm_price
        temp2 = max(0, i-extra_num) * extra_price
        temp_all = temp1 + temp2
        summer += 0 if temp_all <= limit else temp_all
    print('%.2f' % summer)

better_call_saul()
