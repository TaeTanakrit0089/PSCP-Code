'''Saul Goodman'''


def better_call_saul(textfrom, textto):
    '''I'll fight for you Albuquerque!'''
    temp = textfrom
    # firstphase
    for i in range(1, len(textto)+2):
        print(temp)
        temp = textto[:i] + textfrom[i:]
        lastrun = textfrom[i:]
    if temp == textto:
        return 0
    textfrom = lastrun
    if len(textfrom) > len(textto):
        for i in range(len(textfrom)+1):
            temp = textto + textfrom[i:]
            print(temp)


better_call_saul(input(), input())
