'''pre'''


def main():
    '''pre'''
    num1 = int(input())
    num_input = []
    for i in range(num1):
        temp = [float(input()), float(input())]
        num_input.append(temp)

    avg_cost = []
    for i in num_input:
        temp = i[0] / i[1]
        avg_cost.append(temp)

    print_position = avg_cost.index(min(avg_cost))
    result = num_input[print_position]
    print("%.02f %.02f" % (result[0], result[1]))


main()
