'''Can't do Math? Call Peter Griffin'''
import time
'''
-688434860738661209029109331724171101088947635815506406400454753
Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj.
'''
'''
    condi1 = point_a[0][0] == point_a[1][0] or point_a[0][1] == point_a[1][1] \
        or point_b[1][0] == point_b[0][0] or point_b[0][1] == point_b[1][1]
    condi2 = point_a[0][0] > point_b[1][0] or point_b[0][0] > point_a[1][0]
    condi3 = point_a[0][1] > point_b[0][1] or point_b[1][1] > point_a[0][1]
'''
def bench_time():
    print()
    x = int(input())
    y = input()
    print()
    start_time = time.time()
    print(better_call_saul(x, y))
    print("Process finished --- %f seconds ---" % (time.time() - start_time))


def bench_time_test1():
    print()
    x = int(input())
    y = input()
    print()
    start_time = time.time()
    print(better_call_saul(x, y))
    print("Process finished --- %f seconds ---" % (time.time() - start_time))


def test1(step, text):
    """ _ """

    newstring = ""
    for i in text:
        if i.isalpha():
            if i.islower():
                i = ord(i) - ord('a')
                isupper = False
            else:
                i = ord(i) - ord('A')
                isupper = True
            i = (i + step) % 26

            if isupper:
                i = chr(i + ord('A'))
            else:
                i = chr(i + ord('a'))
        newstring += i
    return (newstring)


def better_call_saul(direction, text, new_text=''):
    '''The Constitution says you do, and so do I.'''
    if direction % 26 == 0:
        return text
    for i in text:
        if i.isupper():
            as_range = [65, 90]
        elif i.islower():
            as_range = [97, 122]
        else:
            new_text += i
            continue
        direction = (abs(direction) % 26) * (direction // abs(direction))
        temp1 = ord(i) + direction
        if temp1 < as_range[0]:
            temp1 += 26
        if temp1 > as_range[1]:
            temp1 -= 26
        new_text += chr(temp1)
    return new_text


bench_time_test1()
