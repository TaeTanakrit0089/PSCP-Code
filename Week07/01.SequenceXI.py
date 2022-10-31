"""Monterey"""


def main():
    """Monterey"""
    num_input = int(input())
    num1 = num_input*2 - 1
    mat = [[' ' for j in range(num1)]for i in range(num1)]

    temp = 1
    all_len = num1
    first_row = 0
    last_row = all_len-1

    for num_change in range(num_input):
        for i in range(temp-1, last_row+1):
            for j in range(temp-1, last_row+1):
                if i == first_row or i == last_row or\
                        j == first_row or j == last_row:
                    mat[i][j] = temp
        num_change = num_change
        temp += 1
        first_row += 1
        last_row -= 1

    for i in mat:
        for j in i:
            print("%02d" % j, end=' ')
        print()


main()
