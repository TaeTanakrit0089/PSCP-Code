'''Pre'''


def jumping():
    '''Pre'''
    print_output(1)
    print_output(1)
    print_output(1)
    print_output(2)
    print_output(2)
    print_output(2)
    print_output(3)
    print_output(3)
    print_output(3)
    print_output(4)
    print_output(4)
    print_output(4)
        
def print_output(num):
    '''0'''
    print('Output%d' % num)


jumping()


for i in range(4):
        for j in range(3):
            print_output(i+1)