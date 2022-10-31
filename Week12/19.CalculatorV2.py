'''Saul Goodman'''
def do_math(num_cal):
    '''Saul Goodman'''
    if num_cal <= 1:
        return 1
    word_length, result = len(str(num_cal)), 0
    for i in range(word_length):
        start_num, end_num = int('1' + '0'*(i-1)), int('9' + '9'*(i-1))
        result += i * (end_num - start_num + 1)
        last_run = 10**i
    return result + num_cal + (word_length * (num_cal-last_run+1))
print(do_math(int(input())))
