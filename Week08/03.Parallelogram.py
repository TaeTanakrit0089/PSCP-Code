"""Python"""

def main():
    """Python"""
    text1 = input()
    text_len = len(text1)

    space = text_len - 1
    text_left = 1
    for i in range(text_len-1):
        print(' ' * space, end='')
        print(text1[:text_left])
        space -= 1
        text_left += 1

    for i in range(text_len):
        print(text1[i:])


main()
