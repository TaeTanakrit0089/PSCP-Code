'''Saul Goodman'''

def main(text_before):
    '''Saul Goodman'''
    text = text_before
    temp = ''
    count = False
    for i in text_before:
        if i == '<':
            count = True
        if count:
            temp += i
        if i == '>':
            count = False
            text = text.replace(temp, ' ')
            temp = ''
    text = text.split()
    print(text)

main(input())
