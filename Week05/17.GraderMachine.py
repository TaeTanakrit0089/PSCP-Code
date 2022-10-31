"""Yo! Mr.White"""


def breaking_bad():
    "Waltauh, put you * away Waltauh"
    gustavo_fring = int(input())
    hank_schrader = int(input())
    skyler_white = 0

    print("pass :", end='')
    if gustavo_fring < hank_schrader:
        for i in range(gustavo_fring, hank_schrader+1):
            if i % 2 == 0:
                print(" %d" % i, end='')
                skyler_white += i
    else:
        for i in range(gustavo_fring, hank_schrader-1, -1):
            if i % 2 == 0:
                print(" %d" % i, end='')
                skyler_white += i
    print()
    print("Sum : %d" % skyler_white)


breaking_bad()
