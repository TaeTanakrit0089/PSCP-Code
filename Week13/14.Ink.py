'''the world is coming to the end?'''
from math import ceil
def better_call_saul():
    '''Better Call Saul!!!! He is going to sue the giant-ink'''
    temp = input().split()
    ink_spread, all_people = int(temp[0]), int(temp[1])
    for _ in range(all_people):
        temp = input().split()
        temp1, temp2 = int(temp[0]), int(temp[1])
        home_area = ((temp1)**2+(temp2)**2) * 3.1416
        print(ceil(home_area / ink_spread))

better_call_saul()
