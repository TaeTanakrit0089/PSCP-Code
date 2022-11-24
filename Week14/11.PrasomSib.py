"""I'm burnin' through the sky, yeah
200 degrees, that's why they call me Mister Fahrenheit"""
def dont_stop_me_now():
    """I'm travelling at the speed of light
    I wanna make a supersonic man out of you"""
    in_num, summer, temp = input(), 0, 0
    for i in range(len(in_num)-1):
        for j in in_num[int(i):]:
            temp += int(j)
            if temp == 10:
                summer += 1
                break
        temp = 0
    return summer
print(dont_stop_me_now())
