'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul(number):
    '''The Constitution says you do, and so do I.'''
    before, stat = ['1', '2'], 1
    while stat != number:
        before.append(before[0] + before[1])
        before.pop(0)
        stat += 1
    return before[0][::-1]

print(better_call_saul(int(input())))
