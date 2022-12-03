'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    all_socks, all_count = input(), {}
    nodup, summer = sorted(set(all_socks)), 0
    for i in nodup:
        all_count[i] = all_socks.count(i) // 2

    if max(all_count.values()) == 0:
        print('None', end='')
    else:
        for all_words, all_count in all_count.items():
            temp1 = all_words * 2
            for i in range(all_count):
                print(temp1, end=' ')
            summer += all_count
    print()
    print(summer)

better_call_saul()
