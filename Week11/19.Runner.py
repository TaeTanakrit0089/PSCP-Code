'''Saul Goodman'''
def better_call_saul(distance, all_guy):
    '''I'll fight for you Albuquerque!'''
    data, all_run = [input().split() for i in range(all_guy)], []
    for i in range(all_guy):
        distance_left = distance - int(data[i][1])
        time_to_run = distance_left/int(data[i][0])
        all_run.append([i+1, time_to_run, int(data[i][0])])
    all_run.sort(key=lambda l: l[2], reverse=True)
    all_run.sort(key=lambda l: l[1])
    print(all_run[0][0])

better_call_saul(int(input()), int(input()))
