"""weight"""


def main():
    """input"""
    num_avg = float(input())
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = (num_avg * 4) - (num1 + num2 + num3)
    print(num4)

    if num1 + num2 + num3 + num4 >= 15000:
        print("Overweight")
    elif unbalance(num1, num2, num3, num4, num_avg):
        print("Unbalance")
    else:
        print("Pass %.2f" % num4)


def unbalance(num1, num2, num3, num4, num_avg):
    '''pre'''
    weight = [num1, num2, num3, num4]
    half_avg = num_avg / 2
    if abs(num1-num2) >= half_avg or abs(num1-num3) >= half_avg\
            or abs(num1-num4) >= half_avg:
        return True
    elif abs(num2-num1) >= half_avg or abs(num2-num3) >= half_avg\
            or abs(num2-num4) >= half_avg:
        return True
    elif abs(num3-num1) >= half_avg or abs(num3-num2) >= half_avg\
            or abs(num3-num4) >= half_avg:
        return True
    elif abs(num4-num1) >= half_avg or abs(num4-num3) >= half_avg\
            or abs(num4-num2) >= half_avg:
        return True
    return False

main()
