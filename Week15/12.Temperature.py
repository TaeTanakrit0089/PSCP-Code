"""LOS POLLOS HERMANOS"""


def main():
    """LOS POLLOS HERMANOS"""
    temp = float(input())
    t_from = input().upper()
    t_to = input().upper()
    changef(t_to, convert(t_from, temp))


def convert(ding1, ding2):
    """LOS POLLOS HERMANOS"""
    if ding1 == "F":
        return float((ding2-32) / 9)
    elif ding1 == "C":
        return float(ding2 / 5)
    elif ding1 == "K":
        return float((ding2-273.15) / 5)
    elif ding1 == "R":
        return float((ding2 - 491.67) / 9)


def changef(ding1, ding2):
    """LOS POLLOS HERMANOS"""
    if ding1 == "F":
        print("%.2f" % float((ding2*9)+32))
    elif ding1 == "K":
        print("%.2f" % float((ding2 * 5) + 273.15))
    elif ding1 == "R":
        print("%.2f" % float((ding2 * 9) + 491.67))
    elif ding1 == "C":
        print("%.2f" % float(ding2 * 5))


main()
