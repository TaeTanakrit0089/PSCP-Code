'''Saul Goodman, attorney at law, 505-164-CALL.'''
def better_call_saul():
    '''That's 505-164-CALL.'''
    numpad = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL',
              6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
    word = ''
    for _ in range(int(input())):
        num_pad, time_click = int(input()), int(input())
        if num_pad == 1:
            word = word[:-time_click]
            continue
        time_click = (time_click-1) % len(numpad[num_pad])
        word += numpad[num_pad][time_click]
    if word.isspace() or not word:
        return  'null'
    return word

print(better_call_saul())
