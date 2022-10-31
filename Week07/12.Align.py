'''Saul Goodman'''


def con_man_albuquerque():
    '''I type-in .. and you pop up big as day'''
    space = int(input())
    text_type = input().lower()
    text_input = input()

    if text_type == 'left':
        left_align(space, text_input)
    elif text_type == 'center':
        center_align(space, text_input)
    elif text_type == 'right':
        right_align(space, text_input)


def left_align(space, text_input):
    '''The fact is, Walter White couldn't have done it without me'''
    text_len = len(text_input)
    space_need_to_be_created = space - text_len
    print(text_input, end='')
    print(' '*space_need_to_be_created)


def right_align(space, text_input):
    '''Mr. Goodman, sit down and stay seated.'''
    text_len = len(text_input)
    space_need_to_be_created = space - text_len
    print(' '*space_need_to_be_created, end='')
    print(text_input)


def center_align(space, text_input):
    '''The name's McGill. I'm James McGill.'''
    text_len = len(text_input)
    space_need_to_be_created = space - text_len
    if space_need_to_be_created % 2 == 1:
        space_need_to_be_created_left = space_need_to_be_created//2 + 1
        space_need_to_be_created_right = space_need_to_be_created//2
    else:
        space_need_to_be_created_left = space_need_to_be_created // 2
        space_need_to_be_created_right = space_need_to_be_created // 2
    print(' '*space_need_to_be_created_left, end='')
    print(text_input, end='')
    print(' '*space_need_to_be_created_right,)


con_man_albuquerque()
