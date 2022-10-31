"""Ball"""


def main():
    """Ball"""
    num_input = int(input())
    #all_input = [input().strip() for i in range(num_input)]

    for i in range(num_input):
        text_input = input().strip()

        if text_input.isidentifier() or not find_space(text_input)\
                and check_restricted_word(text_input):
            print('Valid')
        else:
            print('Invalid')

   # for i in all_input:
        # if i.isidentifier() and not find_space(i) and check_restricted_word(i):
            # print('Valid')
        # else:
            # print('Invalid')


def find_space(text):
    '''Saul Goodman'''
    for i in text:
        if i.isspace():
            return True
        return False


def check_restricted_word(text):
    if text == 'if' or text == 'else' or text == 'elif' or text == 'while'\
            or text == 'for' or text == 'True' or text == 'False' or text == 'continue'\
            or text == 'break' or text == 'return' or text == 'is' or text == 'in' or text == 'and'\
            or text == 'or' or text == 'from' or text == 'as' or text == 'pass' or text == 'not'\
            or text == 'not' or text == 'def' or text == 'none':
        return False
    return True


main()
