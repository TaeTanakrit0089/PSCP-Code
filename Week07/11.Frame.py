"""Frame"""


def frame():
    """Frame"""
    text1 = input()
    len_text1 = len(text1)

    print('*'*(len_text1+2))
    print('*'+text1+'*')
    print('*'*(len_text1+2))


frame()
