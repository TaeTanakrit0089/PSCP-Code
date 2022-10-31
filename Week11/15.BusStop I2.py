'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    passenger = int(input())
    busstop = int(input())
    in_bus, count = [], 0
    all_input = [input().split() for i in range(busstop)]
    all_bus_stop = [int(i[0]) for i in all_input]
    stop_passed = []
    count, passenger_count = -1, 0
    for i in all_bus_stop:
        print(in_bus)
        count += 1
        temp = all_input[count][1:]
        temp = [int(i) for i in temp]

        for _ in range(in_bus.count(i)):
            in_bus.remove(i)
        for j in temp:
            if len(in_bus) >= passenger:
                break
            condi1 = j <= i
            condi2 = j not in all_bus_stop and j in stop_passed
            if condi1 or condi2:
                continue
            in_bus.append(j)
            passenger_count += 1
        stop_passed.append(i)
    print(passenger_count)


main()
