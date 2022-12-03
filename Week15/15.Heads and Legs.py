'''i see a little silhouetto of the pigeons'''
def freddiemercury(galileo_a, galileo_b):
    '''Four pigeons are looking at me, very, very frightening me'''
    birds, rabbit = (4*galileo_a-galileo_b)/2, (galileo_b-2*galileo_a)/2
    if rabbit < 0 or birds < 0 or rabbit % 1 != 0 or birds % 1 != 0:
        print('Impossible')
    else:
        print('%d %d' % (rabbit, birds))
freddiemercury(int(input()), int(input()))


