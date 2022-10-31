'''Pre'''


def digit():
    '''Pre'''

    num_input = input()
    while num_input != '0':
        num_result = str(num_input)
        while len(num_result) > 1:
            temp = 0
            for i in num_result:
                temp += int(i)
            num_result = str(temp)

        print(num_result)
        num_input = input()

digit()
