"AlmostMean"
def main():
    "AlmostMean"
    number = [input().split() for _ in range(int(input()))]
    number = sorted(number, key=lambda x:float(x[1]))
    scr = 0
    for i in number:
        scr += float(i[1])
    med = scr/len(number)
    number = sorted(number, key=lambda x:float(x[1]), reverse=True)
    for i in number:
        if float(i[1]) < med:
            print(*i, sep='\t')
            break
main()
