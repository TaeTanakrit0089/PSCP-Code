'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    number, all_perfect = int(input()), []
    for count in range(2, number):
        if find_proper_divisors(count):
            temp = (2 ** (count - 1)) * ((2 ** count) - 1)
            if temp > number:
                break
            elif temp <= number and temp not in all_perfect:
                all_perfect.append(temp)
    print(sum(all_perfect))


def find_proper_divisors(num):
    '''Saul Goodman'''
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


better_call_saul()
