'''Can't do Math? Call Peter Griffin'''
 
#75683497543895743895748237589432758974235897024358972043542342307
#4983999726786007986008272569791458981188458092496581043762683481216
 
def do_math(num_cal):
    '''DO MATH'''
    if num_cal <= 9:
        if num_cal <= 1:
            return 1
        else:
            return num_cal * 2
    word_length = len(str(num_cal))
    result = 0
    for i in range(1, word_length):
        result += cal_num_range(i)
        last_run = 10**i
    result += word_length * (num_cal-last_run+1)
    return result + num_cal
 
def cal_num_range(size):
    '''Peter Griffin'''
    start_num = int('1' + '0'*(size-1))
    end_num = int('9' + '9'*(size-1))
    all_type = end_num - start_num + 1
    return size * all_type
 
print(do_math(int(input())))