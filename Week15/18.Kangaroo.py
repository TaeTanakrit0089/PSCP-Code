"""Steve walks warily down the street"""
def another_one_bite_the_dust(num_a, num_b, num_c):
    """With his brim pulled way down low"""
    return max(num_c-num_b, num_b-num_a) - 1
print(another_one_bite_the_dust(int(input()), int(input()), int(input())))
