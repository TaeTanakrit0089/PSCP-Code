'''pre'''

def main():
    '''pre'''
    num_n = int(float(input()) * 100)
    num_k = int(input())

    for i in range(num_k):
        num_n = num_n * 10381 // 10000
        i = i

    print("%d.%02d" % (num_n//100, (num_n%100)))

main()
