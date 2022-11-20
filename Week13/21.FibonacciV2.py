'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul(number, data):
    """ Return fibonacci values for given number """
    if number in data:
        return data[number]
    if number > 500:
        better_call_saul(number - 500, data)
    result = better_call_saul(number-2, data) + better_call_saul(number-1, data)
    data[number] = result
    return result
print(better_call_saul(int(input()), {0: 0, 1: 1}))
