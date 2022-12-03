'''Saul Goodman'''

def better_call_saul():
    '''Saul Goodman'''
    data = [int(input()) for  _ in range(int(input()))]
    for i in data:
        los_pollos_hermanos(i)

def los_pollos_hermanos(num1):
    '''POLLOS'''
    temp1, all_possible = 2, []
    while temp1 != num1:
        if num1 % temp1 == 0:
            all_possible.append(temp1)
            num1 /= temp1
        else:
            temp1 += 1
    all_possible.append(temp1)
    merge_all_num(all_possible)

def merge_all_num(data):
    '''FREDDIE MERCURY'''
    nodup, all_count = sorted(set(data)), {}
    for i in nodup:
        all_count[i] = data.count(i)

    for num, dupp in all_count.items():
        if dupp == 1:
            print(num, end='')
        else:
            print('%d**%d' % (num, dupp), end='')
        if num != nodup[-1]:
            print(' x ', end='')
    print()

better_call_saul()
