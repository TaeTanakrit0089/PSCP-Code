'''Pre'''


def func_cir():
    '''ppp'''
    numx = float(input())
    numy = float(input())
    numr = float(input())
    numxn = float(input())
    numyn = float(input())

    if (numxn-numx)**2 + (numyn-numy)**2 <= numr**2:
        print("True")
    else:
        print("False")


func_cir()
