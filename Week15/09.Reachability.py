'''Saul Goodman'''
import json
def huell():
    '''Saul Goodman'''
    data, node = json.loads(input().replace("'", '"')), input()
    linked, before = data[node], []
    while 1:
        temp = [node]
        for i in linked:
            temp += data[i]
        linked = sorted(list(dict.fromkeys(temp)))
        if linked == before:
            break
        before = linked
    print(linked)
huell()
