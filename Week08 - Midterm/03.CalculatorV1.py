'''Can't do Math? Call Peter Griffin'''
def do_math(num_cal):
    '''DO MATH'''
    if num_cal <= 1:
        return 1
    result = 0
    for i in range(1, num_cal+1):
        result += len(str(i)) + 1
    return result
 
print(do_math(int(input())))
