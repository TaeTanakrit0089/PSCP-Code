'''prepro'''
def main():
    '''Prepro'''
    temp, text = input(), []
    while temp != "NULL":
        text.append(temp)
        temp = input()
    print(*text[::-1], sep='\n')
main()
