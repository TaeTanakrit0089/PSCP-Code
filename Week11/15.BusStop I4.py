'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    passenger = int(input())
    all_stop = int(input())
    data = []
    for _ in range(all_stop):
        data.append([int(i) for i in input().split()])
    data.sort(key=lambda l: l[0])
    in_bus, passenger_pass = [], 0
    for i in data:
        current_stop = i[0]
        if len(in_bus) > 0:
            temp = in_bus.copy()
            for j in in_bus:
                if j == current_stop:
                    temp.remove(j)
                    passenger_pass += 1
            in_bus = temp

        for j in i[1:]:
            if len(in_bus) == passenger:
                break
            if current_stop < j:
                in_bus.append(j)
    print(passenger_pass)


better_call_saul()
