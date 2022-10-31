"""Ball"""


def main():
    """Ball"""
    num_input = float(input())
    num_count = -1
    while num_input >= 1/100:
        num_input = num_input * 3 / 5
        num_count += 1
    print(num_count)


main()
