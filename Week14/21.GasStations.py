'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    all_distance, full_tank, all_gas = int(input()), int(input()), int(input())
    gas_station = [int(input()) for i in range(all_gas)]
    each_length = [gas_station[0]] + [(gas_station[i+1] - gas_station[i]) for i in range(all_gas-1)]
    car, count = full_tank, 0
    for i in range(1, len(each_length)):
        car -= each_length[i-1]
        if car < each_length[i+1]:
            car = full_tank
            count += 1
    print(count)
lwyrup()
