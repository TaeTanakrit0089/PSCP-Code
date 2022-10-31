def main():
    num = int(input())
    all_score = [input().split() for i in range(num)]

    avg = 0
    for i in all_score:
        i[1] = float(i[1])
        avg += i[1]
    avg = avg / num
    all_score.sort(key=lambda l:l[1])


    last_run = []
    for i in all_score:
        if i[1] >= avg:
            break
        last_run = i
    print(*last_run, sep='\t')

main()
