'''Can't do Math? Call Peter Griffin'''

def do_math(num_a, num_b, num_c):
    '''DO MATH'''
    num_s = (num_a+num_b+num_c) / 2
    num_final = num_s * (num_s-num_a) * (num_s-num_b) * (num_s-num_c)
    return ('%.03f') % num_final ** 0.5

print(do_math(float(input()), float(input()), float(input())))
