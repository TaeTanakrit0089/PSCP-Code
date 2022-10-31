'''OH! I'm wanna drink some soda!!!'''
def better_drink_coke(percan, cap, dispercan, atleast):
    '''Better Call Cola-Cola'''
    result = 0
    if cap <= 0:
        result = percan * atleast
    else:
        temp1 = 0
        for i in range(atleast):
            if temp1 == cap:
                result += dispercan
                temp1 = 0
            else:
                result += percan
            temp1 += 1
    print(result)

better_drink_coke(int(input()), int(input()), int(input()), int(input()))
