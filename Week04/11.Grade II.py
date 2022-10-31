'''Pre'''


def main():
    '''Pre'''
    num_1 = float(input())
    if num_1 > 100 or num_1 < 0:
        print("ERR")
    elif num_1 >= 95:
        print("A")
    elif num_1 >= 90:
        print("B+")
    elif num_1 >= 85:
        print("B")
    elif num_1 >= 80:
        print("C+")
    elif num_1 >= 75:
        print("C")
    elif num_1 >= 70:
        print("D+")
    elif num_1 >= 65:
        print("D")
    elif num_1 >= 60:
        print("F+")
    elif num_1 <= 60:
        print("F")

main()
