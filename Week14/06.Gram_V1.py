'''Hi, I'm Saul Goodman. Did you know that you have rights?'''
def lwyrup():
    '''The constitution says you do! And so do I.'''
    text, sub, count = input(), [], {}
    for i in range(1, len(text)):
        for j in range(0, len(text) - i):
            sub.append(text[j:i+j+1])
    for key in sub:
        count[key] = text.count(key)
    print(*sorted(count.items(), key=lambda l:l[1] ,reverse=1)[0], sep='\n')

lwyrup()
