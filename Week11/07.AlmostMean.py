'''prepro'''


def main():
    '''Prepro'''
    num = int(input())
    student = [input().split() for i in range(num)]
    average = [float(student[i][1]) for i in range(num)]

    # find average
    count = 0
    for i in average:
        count += i
    average = count / num

    least = 999999
    least_guy = ''
    for i in student:
        temp = abs(average - float(i[1]))
        if temp <= least:
            least = temp
            least_guy = i

    print(*least_guy, sep='\t')


main()
