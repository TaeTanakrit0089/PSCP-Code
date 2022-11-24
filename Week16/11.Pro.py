'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    come, pay = int(input()), int(input())
    per_guys, all_guys = int(input()), int(input())
    temp1, temp2 = all_guys // come, all_guys % come
    return (temp1 * pay * per_guys) + (temp2*per_guys)

print(better_call_saul())
