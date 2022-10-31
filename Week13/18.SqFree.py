'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''

def better_call_saul(num):
    '''The Constitution says you do, and so do I.'''
    all_sqfree = []
    for i in range(1, num+1):
        if sq_free(i):
            all_sqfree.append(i)
    print(len(all_sqfree))

def sq_free(num):
    '''Saul Goodman'''
    for i in range(2, int(num**0.5)+1):
        if num % (i**2) == 0:
            return False
    return True

better_call_saul(int(input()))
