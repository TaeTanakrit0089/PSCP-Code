'''Saul Goodmain'''


def main():
    ''''Saul Goodmain'''
    highest_step = int(input())
    step_amount = int(input())
    temp = 0
    all_step = 0
    for i in range(step_amount):
        num_input = int(input())
        temp += num_input

        if i+1 == step_amount or highest_step == 0:
            if num_input > highest_step:
                print('NO')
                return 0
            else:
                all_step += 1
                break

        if temp >= highest_step:
            all_step += 1
            temp = 0
    print(all_step)


main()
