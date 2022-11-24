'''Saul Goodman'''
def better_call_saul():
    '''Saul Goodman'''
    unit, tens, hundreads = convert_to_set(
        input()), convert_to_set(input()), convert_to_set(input())
    result = set()
    for i in hundreads:
        for j in tens:
            for k in unit:
                temp = str(i) + str(j) + str(k)
                result.add(temp)
    print(*sorted(result), sep='\n')

def convert_to_set(text):
    '''Saul Goodman'''
    text, final = text.split(), set(i for i in range(10))
    text[1] = int(text[1])
    if text[0] == '!=':
        final.remove(text[1])
    elif text[0] == '==':
        final = set([text[1]])
    elif '>' in text[0]:
        final = set(i for i in range(text[1]+1, 10))
        if '=' in text[0]:
            final.add(text[1])
    elif '<' in text[0]:
        final = set(i for i in range(0, text[1]))
        if '=' in text[0]:
            final.add(text[1])
    return final

better_call_saul()
