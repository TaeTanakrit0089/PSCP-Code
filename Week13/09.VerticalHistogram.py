'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    text_input = input()
    data = do_text_thing(text_input)
    all_count = count_text(text_input)
    max_text = all_count[max(all_count, key=all_count.get)]

    graph = []
    for i in range(max_text, 0, -1):
        temp1 = '%03d' % i
        temp2 = draw_lines(data, all_count, i)
        graph.append([temp1, temp2])

    # print
    for i in graph:
        print(*i, sep=' ')
    print('   ', *data, sep=' ')

def count_text(text):
    '''I believe that until proven guilty,'''
    counted = dict.fromkeys(text)
    for keys, _ in counted.items():
        temp = text.count(keys)
        counted.update({keys: temp})
    return counted

def do_text_thing(text):
    '''every man,woman and child in this country is innocent'''
    data_lower, data_upper = [], []
    for i in text:
        if i.isupper():
            data_upper.append(i)
        elif i.islower():
            data_lower.append(i)
    return list(dict.fromkeys(sorted(data_lower) + sorted(data_upper)))

def draw_lines(data, all_count, current_num):
    '''And that's why I fight for you, Albuquerque!!!'''
    result = ''
    for i in data:
        if all_count[i] >= current_num:
            result += '* '
        else:
            result += '  '
    return result

better_call_saul()
