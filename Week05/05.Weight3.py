"""Saul Goodman"""


def main():
    '''Saul GOodman'''
    avg = float(input())
    weight = [float(input()) for i in range(3)]
    weight_lost = avg*4-weight[0]-weight[1]-weight[2]
    weight.append(weight_lost)
    weight.sort()

    if avg*4 > 15000:
        print("Overweight")
    elif check(weight, avg):
        print("Unbalance")
    else:
        print("Pass %.2f" %weight_lost)
        
    print("Pass %.2f" %weight_lost)
    print(weight)


def check(weight, avg):
    '''Saul Goodman'''
    for i in weight:
        for j in weight:
            if abs(i-j) >= avg/2 :
                return True
    return False


main()
