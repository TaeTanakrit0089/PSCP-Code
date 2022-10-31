'''Hi I'm Saul number, Did You Know That You Have Rights?'''


def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    number = int(input())
    while number:
        temp = [number]
        while number != 1:
            if number % 2 == 0:
                number = number//2
            else:
                number = number*3 + 1
            temp.append(number)
        print(len(temp))
        number = int(input())


better_call_saul()
