'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    next_time = int(input())
    current_time = input()

    hours = int(current_time[:current_time.index(':')])
    miinute = int(current_time[-2:])

    count = 0
    while count != next_time:
        miinute += 1
        if miinute == 60:
            hours += 1
            miinute = 0
        if hours == 24:
            hours = 0

        temp1 = str(hours) + str('%02d' % miinute)
        if temp1 == temp1[::-1]:
            print(str(hours) + ':' + str('%02d' % miinute))
            count += 1


better_call_saul()
