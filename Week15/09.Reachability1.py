'''We're here to make HUELL happy'''
import json
def reasonably():
    '''Are you happy'''
    data, node = json.loads(input().replace("'", '"')), input()
    linked, before = data[node], ['']
    while linked != before:
        before, temp = linked, [node]
        for i in linked:
            temp += data[i]
        linked = sorted(list(dict.fromkeys(temp)))
    print(linked)
reasonably()
