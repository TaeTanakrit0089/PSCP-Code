"""Prayoot"""


def main():
    """Prayoot"""
    num1 = int(input())
    for i in range(num1):
        cal_i = i + 1
        if cal_i % 3 == 0 and cal_i % 5 == 0:
            print("FizzBuzz")
        elif cal_i % 3 == 0:
            print("Fizz")
        elif cal_i % 5 == 0:
            print("Buzz")
        else:
            print(cal_i)


main()
