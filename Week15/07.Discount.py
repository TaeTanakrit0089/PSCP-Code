'''Saul Goodman'''
def huell():
    '''Saul Goodman'''
    temp, book = input(), []
    while temp != 'ENTER':
        book.append(float(temp))
        temp = input()
    if len(book) < 20:
        give_free = len(book) // 6
        if give_free == 3:
            give_free = 2
    else:
        give_free = 4 + ((len(book)-20)//5)
    print('%d' % sum(sorted(book[give_free:])))

huell()
