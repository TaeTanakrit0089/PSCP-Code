'''Saul Goodman'''


def better_call_saul():
    '''I'll fight for you Albuquerque!'''
    all_card, missing_card = [], []
    for _ in range(51):
        missing_card.append(input())
    column, row = ['A', 'K', 'Q', 'J'], ['S', 'H', 'D', 'C']
    for i in row:
        for j in column:
            all_card.append(j+i)
        for j in range(2, 11):
            all_card.append(str(j)+i)
    print(*(set(all_card)-set(missing_card)))


better_call_saul()
