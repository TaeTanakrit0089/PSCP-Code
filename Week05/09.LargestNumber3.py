'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num1 = input()
    num2 = input()
    num3 = input()

    all_possible = [int(num1+num2+num3), int(num1+num3+num2),
                    int(num2+num1+num3), int(num2+num3+num1),
                    int(num3+num2+num1), int(num3+num1+num2)]
    i = 0
    num_m = find_m(all_possible[i], 0)
    i += 1
    num_m = find_m(all_possible[i], num_m)
    i += 1
    num_m = find_m(all_possible[i], num_m)
    i += 1
    num_m = find_m(all_possible[i], num_m)
    i += 1
    num_m = find_m(all_possible[i], num_m)
    i += 1
    num_m = find_m(all_possible[i], num_m)

    print(num_m)


def find_m(num1, num2):
    """Saul Goodman"""
    if num1 > num2:
        return num1
    return num2


main()
