"""Walter White"""


def breaking_bad():
    """Walter White"""
    num_1 = int(input())
    skyler_white = 0

    ehrmantraut = int(input())
    while skyler_white >= 0:
        skyler_white += ehrmantraut
        if skyler_white == num_1:
            return skyler_white
        ehrmantraut = int(input())
        if ehrmantraut == -1 or skyler_white == num_1:
            #print("YO")
            return skyler_white

print(breaking_bad())
