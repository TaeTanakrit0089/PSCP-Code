'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num_input = int(input())
    formula = (num_input-1)//2
    front_space = formula

    for i in range(formula):
        back_space = 2*(i+1) - 3
        if back_space <= 0:
            back_space = 0
        if i == 0:
            back_star = 0
        else:
            back_star = 1

        temp = ' '*front_space + '*' + ' '*back_space + '*'*back_star
        front_space -= 1
        print(temp)

    front_space += 1

    for i in range(formula, -1, -1):
        if i == formula:
            temp = '*'*num_input
            print(temp)
            continue
        back_space = 2*(i+1) - 3
        if back_space <= 0:
            back_space = 0
        if i == 0:
            back_star = 0
        else:
            back_star = 1

        temp = ' '*front_space + '*' + ' '*back_space + '*'*back_star
        front_space += 1
        print(temp)


main()
