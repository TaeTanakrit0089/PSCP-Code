'''Python'''


def main():
    '''Python'''
    day_what = input()
    person_age = float(input())
    person_height = float(input())

    if day_what == 'Senior Day' and person_age >= 60:
        print('FREE')
    elif day_what == 'Children Day' and person_age < 14 and person_height <= 140:
        print('FREE')
    elif person_age < 14 and person_height < 90:
        print('FREE')
    else:
        print('PAY')


main()
