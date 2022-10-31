'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    pics_height = int(input())
    time_loop = int(input())
    pics = [[' ' for i in range(pics_height)] for i in range(pics_height)]
    for i in range(pics_height):
        for j in range(pics_height):
            if i == j or i + j == pics_height - 1 \
                    or j == 0 or i == 0 or j == pics_height - 1 or i == pics_height - 1:
                pics[i][j] = '*'

    for i in range(pics_height):
        for k in range(time_loop):
            for j in range(pics_height):
                print(pics[i][j], end='')
            print(end=' ')
            k = k
        print()


main()
