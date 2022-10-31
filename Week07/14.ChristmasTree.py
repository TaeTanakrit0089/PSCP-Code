'''I was listened this song with my friend last christmas'''


def all_i_want_for_christmas_is_you():
    '''1 year passed by, all gone, never be the same'''
    tree_height = int(input())
    stem_height = int(input())

    tree_space = 2*tree_height - 1
    stem_start_position = tree_space//2 - 1

    tree_leaves = 1
    white_space = tree_height - tree_leaves
    for i in range(tree_height):
        print(' '*white_space, end='')
        print('*'*tree_leaves)
        tree_leaves += 2
        white_space -= 1

    for i in range(stem_height):
        print(' '*stem_start_position, end='')
        print('---')
        i = i


all_i_want_for_christmas_is_you()
