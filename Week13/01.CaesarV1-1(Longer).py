'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul(direction, text, new_text=''):
    '''The Constitution says you do, and so do I.'''
    for i in text:
        if i.isupper():
            ascii_range = [65, 90]
    print(new_text)

def upper_char(alpha, direction):
    '''I believe that until proven guilty, every man, woman and child in this country is innocent'''
    direction = do_direction_thing(direction)
    temp1 = ord(alpha) + direction
    if temp1 < 65:
        temp1 += 26
    if temp1 > 90:
        temp1 -= 26
    return chr(temp1)

def lower_char(alpha, direction):
    '''And that's why I fight for you, Albuquerque!!!'''
    direction = do_direction_thing(direction)
    temp1 = ord(alpha) + direction
    if temp1 < 97:
        temp1 += 26
    if temp1 > 122:
        temp1 -= 26
    return chr(temp1)

def do_direction_thing(direction):
    '''Better Call Saul'''
    temp1 = direction // abs(direction)
    temp2 = (abs(direction) % 26) * temp1
    return temp2

better_call_saul(int(input()), input())
