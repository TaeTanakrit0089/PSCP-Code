'''Saul GOodman'''
def goodman():
    '''Saul Goodman'''
    text = input()
    data = do_text_thing(text)
    for i in data:
        print('%s : %s' % (i, print_lines(text.count(i))))

def print_lines(length):
    '''Saul Goodman'''
    result = ''
    for i in range(length):
        i += 1
        if i % 5 == 0 and i != length:
            result += '-|'
        else:
            result += '-'
    return result

def do_text_thing(temp):
    '''Saul Goodman'''
    text, data_lower, data_upper = [], [], []
    for i in temp:
        text.append(i)
        if i.islower() and i not in data_lower:
            data_lower.append(i)
        elif i.isupper() and i not in data_upper:
            data_upper.append(i)
    data_lower.sort()
    data_upper.sort()
    return data_lower+data_upper

goodman()
