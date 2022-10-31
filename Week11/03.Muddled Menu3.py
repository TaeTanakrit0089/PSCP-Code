'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    data = []
    while 1:
        temp = input()
        if temp == 'DONE':
            break
        elif temp == 'CLOSED':
            data = []
            break
        elif temp == "SOMETHING'S WRONG":
            data = []
        elif "Can't do:" in temp:
            data.remove(temp.replace("Can't do: ", ""))
        else:
            temp = temp.split(' #')
            if temp[1].isnumeric():
                data.insert(int(temp[1]) - 1, temp[0])
            else:
                data.append(temp[0])
    print('Full Course:', data, end=' ')
    print('Reversed:', data[::-1])


better_call_saul()
