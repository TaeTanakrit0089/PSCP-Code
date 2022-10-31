'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    text_input = input()
    unzip = []
    for i in text_input:
        unzip.append(i)
    # unzip.sort()

    final_data = []
    temp = 1
    i = 0
    while True:
        if i+1 == len(unzip):
            final_data.append([temp, unzip[i]])
            break
        if unzip[i] != unzip[i+1]:
            final_data.append([temp, unzip[i]])
            temp = 0
        i += 1
        temp += 1

    for i in final_data:
        print(str(i[0])+str(i[1]), end='')
    print()


better_call_saul()
