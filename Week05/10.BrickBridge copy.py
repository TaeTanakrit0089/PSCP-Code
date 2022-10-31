"""Largestnumber"""
def math(value1, value2):
    if value1 > value2:
        return value1
    return value2

def main():
    """print"""
    num1 = input()
    num2 = input()
    num3 = input()
    ans = num1 + num2 + num3
    ans = math((num1 + num2 + num3), ans)
    ans = math((num1 + num3 + num2), ans)
    ans = math((num2 + num1 + num3), ans)
    ans = math((num2 + num3 + num1), ans)
    ans = math((num3 + num2 + num1), ans)
    ans = math((num3 + num1 + num2), ans)
    print(int(ans))
main()
    

