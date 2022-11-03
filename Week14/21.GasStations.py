'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    all_distance, full_tank, all_gas = float(
        input()), float(input()), int(input())

    if all_distance <= full_tank:
        return 0

    gas_station = [float(input()) for _ in range(all_gas)]
    station_distance = [gas_station[0]] + \
        [gas_station[i+1] - gas_station[i] for i in range(all_gas-1)] + \
        [all_distance - gas_station[-1]]

    car, count = full_tank, 0
    for i in range(len(station_distance)):
        if i+1 == len(station_distance):
            break

        car -= station_distance[i]
        if car < 0:
            return 'depleted'
        if car < station_distance[i+1]:
            count += 1
            car = full_tank

    if car < station_distance[-1]:
        return 'depleted'

    return count


print(lwyrup())
