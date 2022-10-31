"""weight"""
 
 
def main():
    """input"""
    num_avg = float(input())
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = (num_avg * 4) - num1 - num2 - num3
 
    if num_avg * 4 >= 15000:
        print("Overweight")
    elif unbalance(num1, num2, num3, num4, num_avg):
        print("Unbalance")
    else:
        print("Pass %.2f" % num4)
 
 
def unbalance(num1, num2, num3, num4, num_avg):
    '''pre'''
    weight = [num1, num2, num3, num4]
    half_avg = num_avg / 2
    for i in range(3):
        if abs(weight[i] - weight[i+1]) >= half_avg:
            return True
    return False
 
 
main()