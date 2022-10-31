"""Pre"""
 
 
def blue_screen():
    """Pre"""
    num1 = int(input())
    temp = num1-1
    
    for i in range(num1):
        num2 = 1
        for j in range(num1):
            if j >= temp:
                print("%02d" % num2, end=" ")
                num2 += 1
            else:
                print("   ", end='')
        temp -= 1
        print()
        i = i
 
 
blue_screen()