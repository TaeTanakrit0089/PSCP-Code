'''prepro'''


def main():
    '''Prepro'''
    ip_str = input()
    text = input()
    count = 0

    for i in ip_str:
        if i == "1":
            count += 1

    if count % 2 == 0:
        if text == "Even":
            ip_str += "0"
        else:
            ip_str += "1"
    else:
        if text == "Even":
            ip_str += "1"
        else:
            ip_str += "0"

    print(ip_str)


main()
