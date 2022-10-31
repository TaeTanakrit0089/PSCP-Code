'''Olumsa'''


def better_call_saul(num_set):
    '''I'll fight for you Albuquerque!'''
    data = [input().split() for i in range(num_set)]
    country_name, dup = [], []
    for i in data:
        if i[0] not in country_name:
            country_name.append(i[0])
        else:
            dup.append(i[0])
    if dup != []:
        clone_data, data = data, []
        for i in country_name:
            temp = [0, 0, 0]
            for j in clone_data:
                if i == j[0]:
                    temp_data = j
                    del temp_data[0]
                    for k in range(3):
                        temp[i] += temp_data[i]
            data.append([i, *temp])

    data.sort(key=lambda l: l[0])
    data.sort(key=lambda l: l[3], reverse=True)
    data.sort(key=lambda l: l[2], reverse=True)
    data.sort(key=lambda l: l[1], reverse=True)

    rank, rank_skipped = 0, 0
    score_before = [0, 0, 0]
    for i in data:
        score = [int(i[1]), int(i[2]), int(i[3])]
        i.append(sum(score))
        if score == score_before:
            rank_skipped += 1
        else:
            rank += 1 + rank_skipped
            rank_skipped = 0
        score_before = score
        print(rank, *i, sep=' ')

def sumsort(data):
    '''Saul Goodman'''
    return sum(list(map(int, data[1:])))
better_call_saul(int(input()))
