'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    passenger = int(input())
    all_stop = int(input())
    all_data = [input().split() for i in range(all_stop)]
    all_data.sort(key=lambda l:int(l[0]))
    passenger_pass = 0
    all_bus_num = [int(all_data[i].pop(0)) for i in range(all_stop)]
    in_bus, count = [], -1
    for _ in range(all_stop):
        count += 1
        current_station = all_bus_num.pop(0)
        for j in all_data[count]:
            for _ in range(in_bus.count(current_station)):
                in_bus.remove(current_station)
                passenger_pass += 1
            j = int(j)
            if len(in_bus) >= passenger:
                break
            if j not in all_bus_num:
                continue
            in_bus.append(j)
    print(passenger_pass)


better_call_saul()
