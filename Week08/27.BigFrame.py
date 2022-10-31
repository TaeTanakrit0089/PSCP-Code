'''Python'''


def main():
    '''Python'''
    text1 = input().strip()
    text2 = input().strip()
    text3 = input().strip()
    text4 = input().strip()
    text5 = input().strip()

    len_max = max(len(text1), len(text2), len(text3), len(text4), len(text5))

    header = '*' * len_max
    line_1 = '**' + header + '**'

    space_left = len_max - len(text1)
    line_2 = '* ' + text1 + ' '*space_left + ' *'

    space_left = len_max - len(text2)
    line_3 = '* ' + text2 + ' '*space_left + ' *'

    space_left = len_max - len(text3)
    line_4 = '* ' + text3 + ' '*space_left + ' *'

    space_left = len_max - len(text4)
    line_5 = '* ' + text4 + ' '*space_left + ' *'

    space_left = len_max - len(text5)
    line_6 = '* ' + text5 + ' '*space_left + ' *'

    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)
    print(line_6)
    print(line_1)


main()
