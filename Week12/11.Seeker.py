'''Get caught while trying to cheat the exam? Better Call Saul!'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    text = input()
    all_num = []
    temp, count = '', 0
    for i in text:
        count += 1
        if i.isnumeric():
            temp += i
        else:
            if temp != '':
                all_num.append(int(temp))
                temp = ''
        if count == len(text) and temp != '':
            all_num.append(int(temp))
    print(sum(all_num))


better_call_saul()
