'''Hi, I'm Saul Goodman. Did you know that you have rights?'''
def lwyrup():
    '''The constitution says you do! And so do I.'''
    text, summer = input(), -9999999
    all_sub = [(text[i] + text[i+1]) for i in range(len(text)-1)]
    for i in all_sub:
        if all_sub.count(i) > summer:
            biggest, summer = i, all_sub.count(i)
    print(biggest, summer, sep='\n')
lwyrup()
