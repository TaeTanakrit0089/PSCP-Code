'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    per_weight = float(input())
    per_height = float(input()) / 100

    bmi = per_weight / (per_height ** 2)

    if bmi >= 30:
        print("Obese")
    elif bmi >= 25:
        print("Overweight")
    elif bmi >= 18.5:
        print("Normal")
    else:
        print("Underweight")


main()
