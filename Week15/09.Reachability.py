'''Saul Goodman'''
import json
def huell():
    '''Saul Goodman'''
    data, node = json.loads(input().replace("'", '"')), input()
    linked, before = data[node], ['']
    while linked != before:
        before, temp = linked, [node]
        for i in linked:
            temp += data[i]
        linked = sorted(list(dict.fromkeys(temp)))
    print(linked)
huell()
