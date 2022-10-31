'''Saul Goodman'''

def main():
    '''Saul Goodman'''
    num_input = int(input())
    data = [input() for i in range(num_input)]
    data.sort(key=len)
    print(*data, sep='\n')

main()
