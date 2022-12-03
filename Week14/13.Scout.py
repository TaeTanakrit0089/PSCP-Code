"""I'm burnin' through the sky, yeah
200 degrees, that's why they call me Mister Fahrenheit"""
def dont_stop_me_now():
    """I'm travelling at the speed of light
    I wanna make a supersonic man out of you"""
    npq = list(map(int, input().split()))
    egg_weight = sorted(list(map(int, input().split())))
    result, current_weight = 0, 0
    for _ in range(npq[0]):
        if current_weight + egg_weight[0] > npq[2] or result >= npq[1]:
            break
        result += 1
        current_weight += egg_weight.pop(0)
    return result
for _ in range(int(input())):
    print(dont_stop_me_now())
