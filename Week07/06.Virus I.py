"""pre"""


def wannacry():
    """pre"""
    virus_body = input()
    virus_body = virus_body.replace('O', '')
    num_count = 0
    for i in virus_body:
        if i == 'o':
            num_count += 1
        else:
            continue

    print(num_count)


wannacry()
