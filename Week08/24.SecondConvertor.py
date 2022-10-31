"""Python"""


def main():
    """Python"""
    num_k = int(input())
    num_s = int(input())
    num_m = int(input())
    num_h = int(input())

    seconds = num_k
    minutes = seconds//num_s
    seconds = seconds % num_s
    hours = minutes//num_m
    minutes = minutes % num_m
    hours = hours % num_h

    print("%d:%d:%d" % (hours, minutes, seconds))


main()
