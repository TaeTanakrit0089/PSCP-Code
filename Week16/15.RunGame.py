"""Steve walks warily down the street"""
def another_one_bite_the_dust():
    """With his brim pulled way down low"""
    data, summer, last_run = list(map(float, input().split())), 0, 0
    for i in data:
        temp, last_run = abs(i-last_run), i
        summer += temp
    print(round(summer))
another_one_bite_the_dust()
