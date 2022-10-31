'''prepro'''


def main():
    '''Prepro'''
    text_ip = input().split()
    text_ip = [int(i) for i in text_ip]
    text_ip.reverse()
    count = 0
    for i in text_ip:
        if i % 3 == 0 or i % 5 == 0:
            count += 1
            print(i)
    if count == 0:
        print('Nope')


main()
