'''prepro'''


def main():
    '''Prepro'''
    text_ip = input().replace('[', '').replace(']', '')\
        .replace(',', '').split()
    text_ip = [int(i) for i in text_ip]
    count = 0
    for i in text_ip:
        if i % 2 == 0:
            count += 1
            print(i)
    if count == 0:
        print('Nope')


main()
