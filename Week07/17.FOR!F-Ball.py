'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    text_input = input()
    ball_position = 1
    for i in text_input:
        if i == 'A':
            ball_position = ball_a(ball_position)
        elif i == 'B':
            ball_position = ball_b(ball_position)
        elif i == 'C':
            ball_position = ball_c(ball_position)

    print(ball_position)


def ball_a(position):
    '''Jimmy Mcgill'''
    if position == 1:
        return 2
    elif position == 2:
        return 1
    else:
        return position


def ball_b(position):
    '''Jimmy Mcgill'''
    if position == 2:
        return 3
    elif position == 3:
        return 2
    else:
        return position


def ball_c(position):
    '''Jimmy Mcgill'''
    if position == 1:
        return 3
    elif position == 3:
        return 1
    else:
        return position


better_call_saul()
