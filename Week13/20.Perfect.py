'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''

def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    number, perfects = int(input()), []
    for count in range(2, number):
        if isprime(count):
            perfect_number = (2 ** (count - 1)) * ((2 ** count) - 1)
            if perfect_number > number:
                break
            elif perfect_number <= number and perfect_number not in perfects:
                perfects.append(perfect_number)
    print(sum(perfects))

def find_proper_divisors(num):
    '''Saul Goodman'''
    all = []
    if num <= 1:
        return False
    for i in range(2, (num**0.5)+1):
        if num % i == 0:
            return False
    return True

better_call_saul()
