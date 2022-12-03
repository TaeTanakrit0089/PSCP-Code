'''Saul Goodman'''
import json

def better_call_saul():
    '''Saul Goodman'''
    data_in = json.loads(input())
    data = data_in
    num_need, every = int(input()), int(input())
    start_num, stop_num, all_possible = 0, num_need * every, []
    extra_max = 0
    if num_need > len(data):
        new_data = []
        for i in range(0, num_need // len(data_in), every):
            i %= len(data)
            new_data.append(i)
        extra_max = (num_need // len(data_in)) * sum(new_data)
        num_need = num_need % len(data_in)
        data = new_data

    for i in range(len(data_in)):
        temp = extra_max
        num_needeed = num_need
        start_num = i
        stop_num = i + (num_needeed * every)
        for j in range(start_num, stop_num, every):
            j = j % len(data_in)
            temp += data[j]
        all_possible.append(temp)

    print(max(all_possible))

better_call_saul()
