'''Olymsa'''


def olymsa():
    '''Olymsa'''
    data = [input().split() for _ in range(int(input()))]
    data.sort(key=lambda l: l[0])
    for i in range(3, 0, -1):
        data.sort(key=lambda l: l[i], reverse=True)

    before, lastrun = [-1, -1, -1, -1], 1
    for i in range(len(data)):
        gold, silver, copper = int(data[i][1]), int(
            data[i][2]), int(data[i][3])
        sum_all = gold + silver + copper
        current = [gold, silver, copper, sum_all]
        if current != before:
            lastrun = i+1
        data[i].insert(0, lastrun)
        before = current
        data[i].append(sum_all)

    for i in data:
        print(*i)


olymsa()
