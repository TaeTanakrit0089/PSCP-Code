'''Saul Goodman'''
def main():
    '''Saul Goodman'''
    cost_per_bottle = int(input())
    cap = int(input())
    reward = int(input())
    money = int(input())

    all_bottle = money // cost_per_bottle
    all_covers = all_bottle
    while all_covers >= cap and cap > 0:
        temp1 = (all_covers//cap)*reward
        temp2 = all_covers % cap
        all_bottle += temp1
        all_covers = temp1 + temp2
    print(all_bottle)


main()
