'''Saul Goodman'''
import json
def saul_goodman():
    '''Saul Goodman'''
    goodman = input()
    data = {}
    while goodman != 'Start':
        data.update(json.loads(goodman))
        goodman = input()

    goodman = input()
    kill = []
    while goodman != 'End':
        kill.append(goodman)
        goodman = input()

    imposter = 0
    alive, dead = [], []
    for key, value in data.items():
        if key not in kill:
            alive.append([key, value])
            if value == 'Impostor':
                imposter += 1
        else:
            dead.append([key, value])
    alive.sort(key=lambda x: x[0], reverse=False)
    dead.sort(key=lambda x: x[0])
    print('%s Impostor Remains' % imposter)
    print('***Alive***')
    for i in alive:
        print('%s : %s' % (i[0], i[1]))
    print('***Dead***')
    for i in dead:
        print('%s : %s' % (i[0], i[1]))


saul_goodman()
