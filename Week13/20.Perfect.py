'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''

def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    num = int(input())
    all_perfect = []
    for i in range(1, num+1):
        if find_proper_divisors(i):
            all_perfect.append(i)
    print(sum(all_perfect))

def find_proper_divisors(num):
    '''Saul Goodman'''
    all = []
    for i in range(1, (num**0.5)+1):
        if num % i == 0:
            all.append(i)
    return sum(all) == num

better_call_saul()
