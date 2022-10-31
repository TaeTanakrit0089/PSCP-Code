'''Saul Goodman'''


def better_call_saul(thisnum):
    '''I'll fight for you Albuquerque!'''
    prime = True
    if thisnum >= 2:
        for i in range(2, round(thisnum**0.5)+1):
            if thisnum % i == 0:
                prime = False
                break
    else:
        prime = False

    if prime:
        print("YES")
    else:
        print("NO")


better_call_saul(int(input()))
