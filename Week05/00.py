"""pscp"""


from re import L


def my_main():
    """lab-7"""
    people_num = str(input())
    cal_num = 0
    find_how_many = len(people_num)

    # condition 1
    for i in range(0, find_how_many):
        cal_num += int(people_num[i])
        #print("cal_num =", cal_num)
        i += 1

    # condition 2
    find_3_last_turn_back = people_num[::-1]
    #print("find_3_last_turn_back =", find_3_last_turn_back)
    find_3_last = int(find_3_last_turn_back[2] +
                      find_3_last_turn_back[1]+find_3_last_turn_back[0])*10
    #print("find_3_last =", find_3_last)

    # condition 3
    last_result = cal_num + find_3_last
    #print("last_result =", last_result)

    if last_result > 9999:
        last_result = str(last_result)
    elif last_result < 1000:
        last_result += 1000

    if len(last_result) > 4:
        last_result = last_result[1:]
    print(last_result)


my_main()
