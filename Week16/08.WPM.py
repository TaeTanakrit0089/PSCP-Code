'''Saul Goodman'''
def better_call_saul(age, speed):
    '''Saul Goodman'''
    data = {
        'Kids': {'Very Slow': num_range(0, 11), 'Slow': num_range(11, 21),
                 'Average': num_range(21, 31),
                 'Fast': num_range(31, 41), 'Very Fast': num_range(41, 1000)},
        'Adults': {'Very Slow': num_range(0, 26), 'Slow/Beginner': num_range(26, 36),
                   'Intermediate/Average': num_range(36, 46),
                   'Fast/Advanced': num_range(46, 66), 'Very Fast': num_range(66, 81),
                   'Insane': num_range(81, 1000)}
    }
    for key, values in data[age].items():
        if speed in values:
            print(key)
            break

def num_range(start, stop):
    '''Saul Goodman'''
    return set(i for i in range(start, stop))

better_call_saul(input(), int(input()))
