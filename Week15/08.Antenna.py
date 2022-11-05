'''Saul Goodman'''
import json
def huell():
    '''Saul Goodman'''
    radius, ufo_suck = int(input()) * 2, 0
    data = sorted(json.loads(input()))
    if len(data) == 0 or radius == 0:
        return 0
    length = data[0] + radius
    for i in data[1:]:
        if i > length:
            ufo_suck += 1
            length = i + radius
    return ufo_suck+1

print(huell())
