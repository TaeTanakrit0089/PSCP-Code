def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime(num):
        num += 2
    while True:
        if is_prime(num):
            break
        num += 2
    return num

print next_prime(100**10-1) # returns `100000000000000000039`

# benchmark next_prime(100**10-1) using Miller-Rabin algorithm.
1000 calls, 337 per second.
258669 function calls in 2.971 seconds