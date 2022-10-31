"""Saul Goodman"""


def breaking_bad():
    """Saul Goodman"""
    more_than_two = False
    num1 = int(input())
    num2 = float(input())

    score_left = round(num1 - num2)
    all_possible = []
    for i in range(score_left+1):
        if abs(i-(score_left-i)) > 2:
            more_than_two = True
        if i > num2 or score_left-i > num2:
            continue
        if i >= num2 or abs(i-(score_left-i)) < 1:
            break
        all_possible.append([i, score_left-i])

    if not abs(all_possible[0][0] - all_possible[0][1]) > 2:
        print("Not surprising")
    else:
        print("Surprising")

breaking_bad()
