'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
import json

def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    array_input = json.loads(input())
    data = list_slicing(array_input)
    print(sorted(data, reverse=True))

def list_slicing(data):
    '''I believe that until proven guilty,every man,woman and child in this country is innocent'''
    temp = []
    if isinstance(data, list):
        for i in data:
            temp += list_slicing(i)
    else:
        temp.append(data)
    return temp

better_call_saul()
