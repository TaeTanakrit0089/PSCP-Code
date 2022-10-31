'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def better_call_saul(text):
    '''The Constitution says you do, and so do I.'''
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = text
    all_possible = [text]
    for _ in range(25):
        all_possible.append(caesar(1, all_possible[-1]))

    for i in all_possible[::-1]:
        can_be = 0
        i = i.split()
        for j in i:
            for alpha in j:
                if alpha in vowels:
                    can_be += 1
        if can_be >= len(i):
            print(*i)
            return


def caesar(direction, text, new_text=''):
    '''The Constitution says you do, and so do I.'''
    if direction % 26 == 0:
        return text
    for i in text:
        if i.isupper():
            as_range = [65, 90]
        elif i.islower():
            as_range = [97, 122]
        else:
            new_text += i
            continue
        direction = (abs(direction) % 26) * (direction // abs(direction))
        temp1 = ord(i) + direction
        if temp1 < as_range[0]:
            temp1 += 26
        if temp1 > as_range[1]:
            temp1 -= 26
        new_text += chr(temp1)
    return new_text


better_call_saul(input())
