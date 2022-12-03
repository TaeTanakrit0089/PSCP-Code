def time_table(num_from, num_to):
    for i in range(num_from, num_to+1):
        for j in range(1, 13):
            print('%d x %d = %d' % (i, j, i*j))
        print('*'*40)

time_table(int(input()), int(input()))
