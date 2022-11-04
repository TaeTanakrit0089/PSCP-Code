'''Saul Goodman'''
from math import ceil


def huell():
    '''Saul Goodman'''
    score = 0
    circle_r = {0: 5, 2: 5, 4: 4, 6: 3, 8: 2, 10: 1}
    for _ in range(int(input())):
        point = list(map(float, input().split()))
        p_distance = ceil(distance([0, 0], point))
        if p_distance % 2 == 1:
            p_distance += 1
        if p_distance > 10:
            continue
        score += circle_r[p_distance]
    print(score)


def distance(point_a, point_b):
    '''Saul Goodman'''
    temp = (point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2
    return temp ** 0.5


huell()
