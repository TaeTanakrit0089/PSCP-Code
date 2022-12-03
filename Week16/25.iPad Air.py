'''Saul Goodman'''


def main(summer=19900):
    '''Saul Goodman'''
    colors = ['Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue']
    ssd, cellu = ['64', '256'], ['Wi-Fi + Cellular', 'Wi-Fi']
    data = [input() for _ in range(3)]
    if data[0] not in colors or data[1] not in ssd or data[2] not in cellu:
        return 'Not Available'
    summer += 4500 if cellu[0] == data[2] else 0
    summer += 5000 if '256' == data[1] else 0
    return summer


print(main())
