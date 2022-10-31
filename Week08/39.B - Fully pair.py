'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    text_input = input()
    all_char = find_char(text_input)
    final_result = ''
    for i in all_char:
        temp = 0
        for j in text_input:
            if i == j:
                temp += 1
        if temp % 2 == 1:
            final_result += i
    if final_result == '':
        print('fully paired')
    else:
        print(final_result)


def find_char(text1):
    '''Saul Goodman'''
    text_not_sorted = text1
    text1 = sorted(text1)
    text_sorted, final_sort = '', ''
    for i in range(len(text1)):
        if i+1 == len(text1):
            text_sorted += text1[i]
            break
        if text1[i] != text1[i+1]:
            text_sorted += text1[i]

    for i in text_not_sorted:
        if i in text_sorted and not i in final_sort:
            final_sort += i

    return final_sort


main()
