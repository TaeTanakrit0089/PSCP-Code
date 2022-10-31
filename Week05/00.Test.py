def datainput():
    """datainput"""
    saul_1 = input()
    saul_2 = input()
    saul_3 = input()


    num1 = int(saul_1 + saul_2 + saul_3)
    num2 = int(saul_1 + saul_3 + saul_2)
    num3 = int(saul_2 + saul_1 + saul_3)
    num4 = int(saul_2 + saul_3 + saul_1)
    num5 = int(saul_3 + saul_2 + saul_1)
    num6 = int(saul_3 + saul_1 + saul_2)

    if num1 > num2 and num1 > num3 and num1 > num4 and num1 > \
            num5 and num1 > num6:
        print(num1)
    elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > \
            num5 and num2 > num6:
        print(num2)
    elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > \
            num5 and num3 > num6:
        print(num3)
    elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > \
            num5 and num4 > num6:
        print(num4)
    elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > \
            num4 and num5 > num6:
        print(num5)
    elif num6 > num1 and num6 > num2 and num6 > num3 and num6 > \
            num4 and num6 > num5:
        print(num6)
    
 
 
datainput()