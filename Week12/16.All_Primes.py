'''Saul Goodman'''
def find_prime(thisnum):
    '''I'll fight for you Albuquerque!'''
    prime = True
    if thisnum >= 2:
        for i in range(2, thisnum):
            if thisnum % i == 0:
                prime = False
                break
    else:
        prime = False
    return prime

def better_call_saul(num1, count=0):
    '''Saul Goodman'''
    for i in range(2, num1+1):
        if find_prime(i):
            count += 1
    print(count)

better_call_saul(int(input()))
