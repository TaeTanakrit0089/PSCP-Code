'''Saul Goodman'''
import json


def huell():
    '''Saul Goodman'''
    list1, list2 = sorted([json.loads(input()), json.loads(input())], key=len)
    differ = []
    for i in list1:
        if i not in list2:
            differ += [i]
        else:
            list2.remove(i)
    differ += list2
    before_merge, differ = differ, sorted(set(differ))
    if differ == []:
        print('ONAJI DAYO!')
    else:
        for i in differ:
            print(i, before_merge.count(i))


huell()
