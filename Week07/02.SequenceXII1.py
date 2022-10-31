"""Monterey"""


def main():
    """Monterey"""
    num_input = int(input())
    all_row = 2*num_input - 1
    start_num = num_input

    middle_row = num_input - 1
    reverse = False
    start_reverse = False
    for i in range(all_row):
        running_num = start_num
        if running_num < num_input or running_num == 1:
            reverse = False
        else:
            reverse = True
        for j in range(all_row):
            print('%02d' % running_num, end=' ')
            if running_num >= num_input or j == middle_row\
                    or running_num <= 1:
                reverse = not reverse

            if reverse == False:
                running_num += 1
            else:
                running_num -= 1

        if start_num == 1:
            start_reverse = not start_reverse

        if start_reverse == False:
            start_num -= 1
        else:
            start_num += 1

        print()


main()
