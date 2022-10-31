'''Python'''


def main():
    '''Python'''
    numa = float(input())
    numb = float(input())
    numc = float(input())
    numd = float(input())

    first = func_f(func_f(numa))
    second = func_g(func_f(numa-numb))
    third = func_h(func_f(numa+numb), func_f(numa+numc),
                   func_g(func_f(numd**2)))
    four = func_i(func_h(func_f(numa+numb), func_f(numa-numc), func_g(func_f(numd**2)))\
        , func_g(func_f(numa-numb)),
                  func_f(func_f(func_f(func_f(func_f(numc))))), numd**8)

    print(first)
    print(second)
    print(third)
    print(four)


def func_f(num1):
    """ppp"""
    num2 = 2*num1
    return num2


def func_g(num1):
    """ppp"""
    num2 = 3*(num1**4) - (num1**3) + (2*(num1**2)) + 10
    return num2


def func_h(numx, numy, numz):
    """ppp"""
    num2 = ((numz+numx)**2) - (numx*numy) + (numy**2)
    return num2


def func_i(numa, numb, numc, numd):
    """ppp"""
    num2 = ((numa**2)+(numb**2)-(numc**2)) / ((numd**2)-(2*numa*numd)+(2*numa))
    return num2


main()
