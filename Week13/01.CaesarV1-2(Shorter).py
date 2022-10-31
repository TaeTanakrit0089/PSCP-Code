'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul(direction, text, new_text=''):
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

print(better_call_saul(int(input()), input()))
