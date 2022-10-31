'''Saul Goodman'''


from concurrent.futures import BrokenExecutor


def main():
    '''Saul Goodman'''
    num = [int(input()), int(input()), int(input())]
    num_arrange = []
    num_m = find_m(num[0], num[1], num[2])
    num_arrange.append(num_m)
    num.remove(num_m)
    num_m = find_m(num[0], num[1], 0)
    num_arrange.append(num_m)
    num.remove(num_m)
    num_m = find_m(num[0], 0, 0)
    num_arrange.append(num_m)
    num.remove(num_m)

    del num
    num = [str(i) for i in num_arrange]
    del num_arrange
    num_arrange = []

    num_m = find_m(num[0][0], num[1][0], num[2][0])
    num_arrange.append(num_m)
    num_m = find_m(num[0][0], num[1][0], 0)
    num_arrange.append(num_m)
    num_m = find_m(num[0][0], 0, 0)
    num_arrange.append(num_m)
    num.remove(num_m)
    

    print(str(num_arrange[0])+str(num_arrange[1])+str(num_arrange[2]))



def find_m(number_1, number_2, number_3):
    '''pre'''
    number_1 = int(number_1)
    number_2 = int(number_2)
    number_3 = int(number_3)
    high_value = number_1
    if high_value < number_2:
        high_value = number_2
    if high_value < number_3:
        high_value = number_3
    return high_value


main()
