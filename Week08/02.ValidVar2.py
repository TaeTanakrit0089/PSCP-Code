"""Ball"""


def main():
    """Ball"""
    num_input = int(input())
    for i in range(num_input):
        text_input = input().strip()
        condi1 = not text_input.isidentifier()
        condi2 = ' ' in text_input
        condi3 = text_input[0].isnumeric()
        condi4 = check_restric(text_input)

        #print(condi1, condi2, condi3, condi4)
        if condi1 or condi2 or condi3 or condi4:
            print('Invalid')
        else:
            print('Valid')
        i = i


def check_restric(text1):
    '''Saul Goodman'''
    if text1 == 'if' or text1 == 'else' or text1 == 'elif' or text1 == 'while'\
            or text1 == 'for' or text1 == 'True' or text1 == 'False' or text1 == 'continue'\
            or text1 == 'break' or text1 == 'return' or text1 == 'is' or text1 == 'in' \
            or text1 == 'and' or text1 == 'or' or text1 == 'from' or text1 == 'as' or \
            text1 == 'pass' or text1 == 'not'\
            or text1 == 'not' or text1 == 'def' or text1 == 'None':
        return True
    return False


main()
