'''Hi, I'm Saul Goodman. Did you know that you have rights?'''


def lwyrup():
    '''The constitution says you do! And so do I.'''
    num_p, num_q, num_r = int(input()), int(input()), int(input())
    met_a = [[float(input())for j in range(num_q)] for i in range(num_p)]
    met_b = [[float(input())for j in range(num_r)] for i in range(num_q)]

    met = []
    for i in range(num_p):
        first_multi = met_a[i]
        temp0 = []
        for j in range(num_r):
            last_multi = goodman(met_b, j)
            temp1 = 0
            for k in range(len(last_multi)):
                temp1 += first_multi[k] * last_multi[k]
            temp0.append(temp1)
        met.append(temp0)

    for i in met:
        print(*map(int, i))


def goodman(matrix, num):
    '''Saul goodman'''
    temp = []
    for i in range(len(matrix)):
        temp.append(matrix[i][num])
    return temp


lwyrup()
