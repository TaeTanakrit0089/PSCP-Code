'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    text_input, new_data = input().replace('.', '').split(), []
    for i in text_input:
        if gusfring(i):
            continue
        new_data.append(i)
    new_data.sort()
    if new_data == []:
        new_data.append('Nope')
    print(*new_data, sep='\n')

def gusfring(text):
    '''Los Pollos Hermanos'''
    all_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        all_count += text.lower().count(i)
    if all_count < 2:
        return True
    return False
better_call_saul()
