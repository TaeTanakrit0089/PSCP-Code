'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    num_to = int(input())
    all_possible = []
    for i in range(1, num_to+1):
        if i % 3 == 0 or i % 5 == 0:
            all_possible.append(i)
    print(sum(all_possible))


better_call_saul()
