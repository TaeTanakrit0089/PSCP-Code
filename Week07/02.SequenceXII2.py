"""Monterey"""


def main():
    """Monterey"""
    num_input = int(input())
    all_row = num_input*2 - 1

    start_num = num_input
    start_num_reverse = False

    for i in range(all_row):
        running_num = start_num
        if running_num == num_input or running_num == 1:
            running_num_reverse = True
        else:
            running_num_reverse = False

        for j in range(all_row):
            print('%02d' % running_num, end=' ')

            if running_num == 1 or j == num_input - 1\
                    or (running_num == num_input and j != 0):
                running_num_reverse = not running_num_reverse

            if running_num_reverse == False:
                running_num += 1
            else:
                running_num -= 1
        i = i 

        print()

        if start_num == 1:
            start_num_reverse = not start_num_reverse
        if start_num_reverse == False:
            start_num -= 1
        else:
            start_num += 1


main()
