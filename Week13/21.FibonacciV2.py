'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def better_call_saul():
    data = [0, 1]
    for i in range(10000):
        data.append(data[-2] + data[-1])
    before_format = str(data)
    count = 0
    before = ''
    final = ''
    print_next = False
    for i in before_format:
        count += 1
        if count == 95:
            print(i+'\\', end='\n')
            count = 0
            print_next = False
        else:
            print(i,end='')


better_call_saul()
