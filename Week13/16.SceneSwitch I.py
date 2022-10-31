'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    gusfring, data, count = input(), [0], 0
    while gusfring != 'End':
        data.append(float(gusfring))
        gusfring = input()

    status = [True, False, 1]
    for i in range(len(data)):
        space = data[i] - data[i-1]
        all_off = not status[0] and not status[1]
        if space > 6 and all_off:
            status[2] = 0

        if all_off:
            if status[2] == 0:
                status[0] = True
            elif status[2] == 1:
                status[1] = True
        else:
            if status[2] == 0:
                status[2] = 1
            else:
                status[2] = 0
            status[0] = False
            status[1] = False

        if status[1]:
            count += 1
    print(count)

better_call_saul()
