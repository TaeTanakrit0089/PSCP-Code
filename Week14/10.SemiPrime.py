'''Saul Goodman'''


def createSemiPrimeSieve(nnn):
    '''Saul Goodman'''
    vvv = [0 for i in range(nnn + 1)]
    for i in range(1, nnn + 1):
        vvv[i] = i

    countDivision = [0 for i in range(nnn + 1)]

    for i in range(nnn + 1):
        countDivision[i] = 2
    for i in range(2, nnn + 1, 1):
        if (vvv[i] == i and countDivision[i] == 2):
            for j in range(2 * i, nnn + 1, i):
                if (countDivision[j] > 0):
                    vvv[j] = int(vvv[j] / i)
                    countDivision[j] -= 1

    res = 0
    for i in range(nnn + 1):
        if (vvv[i] == 1 and countDivision[i] == 0):
            res += 1
    return res


if __name__ == '__main__':
    '''Saul Goodman'''
    n = int(input())
    semiPrime = createSemiPrimeSieve(n)
    print(semiPrime)
