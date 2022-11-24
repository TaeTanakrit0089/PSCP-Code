"""I'm burnin' through the sky, yeah
200 degrees, that's why they call me Mister Fahrenheit"""
def dont_stop_me_now():
    """I'm travelling at the speed of light
    I wanna make a supersonic man out of you"""
    input()
    all_guys, highest = int(input()), [0, 0]
    data = [int(input()) for _ in range(all_guys)]

    for i in data:
        temp = data.count(i)
        if temp > highest[1]:
            highest = [i, temp]

    highest[0] = 0 if highest[1] <= all_guys / 2 else highest[0]
    print(*highest)
dont_stop_me_now()
