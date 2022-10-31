"""Century"""


def main():
    """Century"""
    num = int(input())
    for i in range(num):
        century = input()
        if century[:4] == "B.E.":
            century = int(century[-4:]) - 543
        else:
            century = int(century[-4:])

        temp = str(century)[-2:]
        first_two = int(str(century)[:2])

        if temp == '00':
            result = first_two
        else:
            result = first_two + 1

        print(result)


main()
