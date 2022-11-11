"""no one can judge you but <e>judge can"""


def my_main():
    """no one can judge you but <e>judge can"""
    get_txt = ((input().lower()).replace(".", "")).replace(" ", "")
    its_list = []
    ans_list = []
    count = 0
    for i in get_txt:
        if i not in its_list:
            its_list.append(i)
    its_list.sort()

    for j in its_list:
        for character in get_txt:
            if character == j:
                count += 1
        ans_list.append([j, count])
        count = 0
    print(sorted(ans_list, key=lambda k: k[1], reverse=True)[0][0])


my_main()
