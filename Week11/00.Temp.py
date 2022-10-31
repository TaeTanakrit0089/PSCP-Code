"""MissingNumber"""


def amin():
    """beom"""
    _ = int(input())
    iii = []
    while True:
        sss = int(input())
        if sss == 0:
            break
        iii.append(sss)
    return iii


def find(iii):
    """find number"""
    number = set(iii)
    output = []
    for i in range(1, iii[-1]):
        if i not in number:
            output.append(i)
        output.sort()
    for i in output:
        return i


print(find(amin()))
