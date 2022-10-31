"""Saul Goodman"""


def main():
    """Saul Goodman"""
    small_rock = int(input())
    big_rock = int(input())
    goal = int(input())

    if big_rock * 5 > goal:
        use_big_rock = goal // 5
    else:
        use_big_rock = big_rock

    big_rock_used = use_big_rock * 5
    goal = goal - big_rock_used

    if goal > small_rock:
        print(-1)
    else:
        print(goal)


main()
