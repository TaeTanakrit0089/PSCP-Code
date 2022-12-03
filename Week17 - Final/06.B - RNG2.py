'''Saul Goodman'''
import json

def better_call_saul():
    '''Saul Goodman'''
    data_in = json.loads(input())
    length = len(data_in)
    num_need, every = int(input()), int(input())
    all_possible = []

    for i in range(length):
        summer = 0
        start_num = i
        end_num = i + (num_need*every)
        data = create_data(data_in, start_num, end_num, every, num_need)
        if num_need > length:
            summer += (num_need // length) * sum(data)
            num_need = num_need % length
            end_num = start_num + (num_need*every)
            for j in range(start_num, end_num, every):
                j %= len(data)
                summer += data[j]
        else:
            summer += sum(data)
        all_possible.append(summer)
        
    print(max(all_possible))

        
def create_data(data, start_num, end_num, every, need):
    '''Saul Goodman'''
    new_data = []
    if need > len(data):
        for j in range(len(data)):
            j %= len(data)
            new_data.append(data[j])
    else:
        for j in range(start_num, end_num, every):
            j %= len(data)
            new_data.append(data[j])
    return new_data
better_call_saul()
