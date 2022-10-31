'''Pre'''


def main():
    'PREE'
    text_ra = int(input())
    text_rb = int(input())
    text_ab = input()

    if text_ab == 'A':
        text_ea = 1/(1+10**((text_rb-text_ra)/400))
    elif text_ab == 'B':
        text_ea = 1/(1+10**((text_ra-text_rb)/400))

    print("%.2f" % round(text_ea, 2))


main()
