'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    data = {'EMF Level 5': ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'],
            'Ghost Writing': ['Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'],
            'Fingerprints': ['Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'],
            'Spirit Box': ['Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith'],
            'Freezing Temperatures': ['Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei'],
            'Ghost Orb': ['Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei']}
    all_ghost = ['Banshee', 'Demon', 'Jinn', 'Mare', 'Oni', 'Phantom',
                 'Poltergeist', 'Revenant', 'Shade', 'Spirit', 'Wraith', 'Yurei']
    ghost = {i: True for i in all_ghost}
    all_evidence = [input() for _ in range(3)]
    for i in all_evidence:
        if i == 'No evidence':
            continue
        current_ghost = data[i]
        for j in ghost:
            if j not in current_ghost:
                ghost[j] = False

    printed = False
    for key, values in ghost.items():
        if values:
            print(key)
            printed = True
    if not printed:
        print('Not yet discovered')


lwyrup()
