'''Saul Goodman'''
import json
def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    score = json.loads(input())
    score1 = dict(sorted(score.items(), key=lambda l: l[0]))
    wanted = float(input())
    saulgone = True
    for key, values in score1.items():
        if values >= wanted:
            print('%s\t%.2f' % (key, values))
            saulgone = False
    if saulgone:
        print('Nope')

better_call_saul()
