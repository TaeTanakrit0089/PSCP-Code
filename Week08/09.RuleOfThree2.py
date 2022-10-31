'''pre'''


def main():
    '''pre'''
    num1 = int(input())
    smallest_price, smallest_weight = float(input()), float(input())
    smallest_calc = smallest_price / smallest_weight

    for i in range(num1-1):
        temp_price, temp_weight = float(input()), float(input())
        calculate = temp_price / temp_weight
        condi1 = calculate <= smallest_calc
        condi2 = calculate == smallest_calc and temp_price > smallest_price
        if condi1 and not condi2:
            smallest_price = temp_price
            smallest_weight = temp_weight
            smallest_calc = calculate
        i = i

    print("%.02f %.02f" % (smallest_price, smallest_weight))


main()
