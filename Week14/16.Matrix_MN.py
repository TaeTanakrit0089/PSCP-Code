'''Hi, I'm Saul Goodman. Did you know that you have rights?'''
def lwyrup(row, column):
    '''The constitution says you do! And so do I.'''
    matrix = [[int(input()) for j in range(column)] for i in range(row)]
    for i in matrix:
        print(*i)

lwyrup(int(input()), int(input()))
