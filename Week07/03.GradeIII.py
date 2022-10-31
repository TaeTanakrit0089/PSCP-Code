"""KMITL"""
from math import floor


def main():
    """KMITL"""
    num1 = int(input())
    num_all = 0
    for i in range(num1):
        num_all += cal_grade(float(input()))
        i = i
    print_value = floor((num_all/num1)*100) / 100
    print("%.2f" % (print_value))


def cal_grade(grade_input):
    """KMITL"""
    if grade_input >= 95:
        return_value = 4
    elif grade_input >= 90:
        return_value = 3.5
    elif grade_input >= 85:
        return_value = 3
    elif grade_input >= 80:
        return_value = 2.5
    elif grade_input >= 75:
        return_value = 2
    elif grade_input >= 70:
        return_value = 1.5
    elif grade_input >= 65:
        return_value = 1
    elif grade_input >= 60:
        return_value = 0.5
    else:
        return_value = 0

    return return_value


main()
