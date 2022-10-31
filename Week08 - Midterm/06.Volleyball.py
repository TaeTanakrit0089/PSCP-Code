'''Saul Goodman'''


def saul_goodman():
    '''Saul Goodman'''
    game = input()
    set_count = 1
    a_win, b_win = 0, 0
    temp_a, temp_b = 0, 0
    game_stat = False
    for i in game:
        if i == 'A':
            temp_a += 1
        else:
            temp_b += 1
        if set_count >= 5:
            win_score = 15
        else:
            win_score = 25
        condi1 = temp_a >= win_score or temp_b >= win_score
        condi2 = abs(temp_b-temp_a) >= 2
        if condi1 and condi2:
            if temp_a > temp_b:
                a_win += 1
            else:
                b_win += 1
            print('Set %d: A (%d) | B (%d)' % (set_count, temp_a, temp_b))
            set_count += 1
            temp_a, temp_b = 0, 0

        if a_win >= 3 or b_win >= 3:
            game_stat = True
            if a_win > b_win:
                winner = 'A'
                win1 = a_win
                win2 = b_win
            else:
                winner = 'B'
                win1 = b_win
                win2 = a_win
            print('%s won %d:%d set'%(winner, win1, win2))
            break
    if not game_stat:
        print('Set %d: A (%d) | B (%d)' % (set_count, temp_a, temp_b))
        print('The game has not finished yet.')

saul_goodman()
