def main():
    num1 = int(input())
    sum_all = 0
    if num1 == 1:
        sum_all = 1
    else:
        for i in range(1,num1+1):
            sum_all += len(str(i)) + 1
    print(sum_all)
main()