'''Olumsa'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    data = []
    for _ in range(int(input())):
        temp = input().split()
        temp_list = [temp[0], list(map(int, temp[1:]))]
        data.append(temp_list)
    data.sort(key=sort_sum, reverse=1)
    data.sort(key=lambda l: l[0])
    data.sort(key=lambda l: l[1], reverse=1)

    rank, rank_skipped = 0, 0
    score_before, sum_before = [], -1
    for i in data:
        score = sum(i[1])
        if i[1] == score_before or sum_before == score:
            rank_skipped += 1
        else:
            rank += 1 + rank_skipped
            rank_skipped = 0
        score_before = i[1]
        print_temp = [rank, i[0]] + i[1] + [score]
        print(*print_temp)


def sort_sum(data):
    '''Saul Goodman'''
    return sum(data[1])


better_call_saul()
