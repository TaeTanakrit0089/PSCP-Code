'''Pre'''


def main():
    '''Pre'''
    num_1 = int(input())
    seconds = num_1
    minutes = seconds//60
    seconds = seconds % 60
    hours = minutes//60
    minutes = minutes % 60
    days = hours//24
    hours = hours % 24

    day_len = len(str(days))
    if day_len > 4:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" % (days, hours, minutes, seconds))


main()
