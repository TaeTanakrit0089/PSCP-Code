def main():
    num = int(input())
    all_score = [input().split() for i in range(num)]

    avg = 0
    for i in all_score:
        i[1] = float(i[1])
        avg += i[1]
    avg = avg / num
    all_score.sort(key=scg,reverse=1)

    for i in all_score:
        if i[1] < avg:
            print(*i,sep='\t')
            break

def scg(text):
    return text[1]

main()
