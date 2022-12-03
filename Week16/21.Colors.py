"""Steve walks warily down the street"""
def another_one_bite_the_dust(color_a, color_b, main_color):
    """With his brim pulled way down low"""
    condi = {('Blue', 'Yellow'): 'Green', ('Blue', 'Red'): 'Violet', ('Red', 'Yellow'): 'Orange'}
    if color_a not in main_color or color_b not in main_color:
        return 'Error'
    elif color_a == color_b:
        return color_b
    return condi[tuple(sorted([color_a, color_b]))]

print(another_one_bite_the_dust(input(), input(), ['Red', 'Yellow', 'Blue']))
