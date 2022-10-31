'''pre'''


def main():
    '''pre'''
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_m = find_m(num_a, num_b, num_c)
    num = [num_a, num_b, num_c]
    num.remove(num_m)
    num.append(num_m)
    if num[0]**2 + num[1]**2 == num[2]**2 or (num[0]**2 + num[1]**2 - num[2]**2 <= 0.01):
        print("Yes")
    else:
        print("No")


def find_m(number_1, number_2, number_3):
    '''pre'''
    high_value = number_1
    if high_value < number_2:
        high_value = number_2
    if high_value < number_3:
        high_value = number_3
    return high_value


main()
