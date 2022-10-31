'''Saul Goodman'''


def better_call_saul(thisnum):
    '''I'll fight for you Albuquerque!'''
    prime = True
    if thisnum >= 2:
        for i in range(2, thisnum):
            if thisnum % i == 0:
                prime = False
                break
    else:
        prime = False

    if prime:
        print("Yes")
    else:
        print("No")


better_call_saul(int(input()))
