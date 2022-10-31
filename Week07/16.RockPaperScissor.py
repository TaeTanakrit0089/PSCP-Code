'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    text = input()
    all_score = [0, 0]
    while len(text) > 0:
        swap_case = text[0]+text[1]
        temp = rock_and_hardplace(swap_case)
        if temp == 'None':
            continue
        for i in range(2):
            all_score[i] = all_score[i] + temp[i]
        text = text[2:]

    if all_score[0] == all_score[1]:
        print('DRAW %d' % all_score[0])
    elif all_score[0] > all_score[1]:
        print('A win %d-%d' % (all_score[0], all_score[1]))
    elif all_score[0] < all_score[1]:
        print('B win %d-%d' % (all_score[1], all_score[0]))


def rock_and_hardplace(swap):
    '''Saul Goodman'''
    first_guy = swap[0]
    second_guy = swap[1]

    return_value = 'None'

    if first_guy == second_guy:
        return_value = [0, 0]   

    elif first_guy == 'R':
        if second_guy == 'P':
            return_value = [0, 1]
        elif second_guy == 'S':
            return_value = [1, 0]

    elif first_guy == 'P':
        if second_guy == 'S':
            return_value = [0, 1]
        elif second_guy == 'R':
            return_value = [1, 0]

    elif first_guy == 'S':
        if second_guy == 'R':
            return_value = [0, 1]
        elif second_guy == 'P':
            return_value = [1, 0]

    return return_value


better_call_saul()
