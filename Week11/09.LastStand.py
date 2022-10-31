'''prepro'''
def main():
    '''Prepro'''
    text_ip = input().replace('[', '').replace(']', '').split(',')
    for i in text_ip : print(i[-1:])
main()