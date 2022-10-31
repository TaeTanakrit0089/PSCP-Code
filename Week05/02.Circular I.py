'''pre'''


def radius():
    '''pre'''
    num_h = float(input())
    num_k = float(input())
    num_r = float(input())
    num_x = float(input())
    num_y = float(input())

    if ((num_h - num_x)**2 + (num_k - num_y)**2)**0.5 <= num_r:
        print("Yes")
    else:
        print("No")


radius()
