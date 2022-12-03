"""I'm burnin' through the sky, yeah
200 degrees, that's why they call me Mister Fahrenheit"""
import json
def dont_stop_me_now():
    """I'm travelling at the speed of light
    I wanna make a supersonic man out of you"""
    goodman, enemy = sorted(json.loads(input())), sorted(json.loads(input()))
    summer, temp1, temp2 = 0, -1, -1
    while temp2 != (len(goodman)*-1)-1:
        if goodman[temp1] > enemy[temp2]:
            summer += goodman[temp1]
            temp1 -= 1
        temp2 -= 1
    print(summer)

dont_stop_me_now()
