"""Steve walks warily down the street"""
def another_one_bite_the_dust():
    """With his brim pulled way down low"""
    tab_ab = {'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4, 'Green': 5,
              'Blue': 6, 'Purple': 7, 'Grey': 8, 'White': 9}
    tab_c = {'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4, 'Green': 5,
             'Blue': 6, 'Purple': 7, 'Gold': -1, 'Silver': -2}
    tab_d = {'Brown': 1, 'Red': 2, 'Green': 0.5, 'Blue': 0.25, 'Purple': 0.1, 'Grey': 0.05,
             'Gold': 5, 'Silver': 10}
    num1, num2 = int(str(tab_ab[input()]) + str(tab_ab[input()])), 10 ** tab_c[input()]
    tolerance, resist = tab_d[input()]/100, num1 * num2
    print('%.4f\n%.4f' % (resist * (1-tolerance), resist * (1+tolerance)))
try:
    another_one_bite_the_dust()
except (ValueError, KeyError):
    print('Error')


