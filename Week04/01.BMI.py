'''Python'''


def main():
    '''Python'''
    find_bmi()
    find_bmi()
    find_bmi()
    find_bmi()
    find_bmi()


def find_bmi():
    '''ppp'''
    per_name = input()
    per_weight = float(input())
    per_height = float(input()) / 100

    bmi = per_weight / (per_height ** 2)

    print("%s's  BMI = %.2f" % (per_name, bmi))


main()
