"""Saul Goodman"""

from math import floor


def breaking_bad():
    """Saul Goodman"""
    all_score = float(input())
    highest_score = float(input())

    score_left = all_score - highest_score
    distance = abs(round(highest_score) - highest_score)
    # print(distance)
    if distance == 0:
        distance = 1
    first_value = 0 - distance
    while True:
        first_value += distance
        second_value = score_left - first_value
        if (first_value >= highest_score and abs(first_value+second_value) == score_left) or\
                (first_value + second_value == score_left and first_value < highest_score and
                 second_value < highest_score):
            break

        #
        # print(first_value, second_value)
    if floor(first_value) - second_value > 2:
        print("Surprising")
    else:
        print("Not surprising")


breaking_bad()
