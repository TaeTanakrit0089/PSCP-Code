'''Saul Goodman'''
def huell():
    '''Saul Goodman'''
    age, weight, usedto, approve = int(
        input()), int(input()), int(input()), True
    if age in range(60, 71) or age == 17:
        if input() == 'False':
            approve = False
    condi1 = weight >= 45
    condi2 = (usedto == 0 and age < 55) or usedto > 0
    condi3 = age in range(17, 71)
    if condi1 and condi2 and condi3 and approve:
        return 'Yes'
    return 'No'

print(huell())
