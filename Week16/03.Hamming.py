'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    first, last, count = input(), input(), 0
    for i in range(len(first)):
        if first[i] != last[i]:
            count += 1
    print(count)
better_call_saul()
