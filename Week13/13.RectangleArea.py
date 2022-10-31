'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''


def better_call_saul():
    '''Credit --> https://www.youtube.com/watch?v=ICtwTFkvFHY&ab_channel=CodeSavant'''
    reg_a, reg_b = input().split(), input().split()
    reg_a, reg_b = [int(i) for i in reg_a], [int(i) for i in reg_b]
    point_a = [[reg_a[0], reg_a[1]], [reg_a[0]+reg_a[2], reg_a[1]+reg_a[3]]]
    point_b = [[reg_b[0], reg_b[1]], [reg_b[0]+reg_b[2], reg_b[1]+reg_b[3]]]

    width_overlap = min(point_a[1][0], point_b[1][0]) -\
        max(point_a[0][0], point_b[0][0])
    height_overlap = min(point_a[1][1], point_b[1][1]) -\
        max(point_a[0][1], point_b[0][1])
    result = width_overlap*height_overlap
    if result <= 10:
        return 'no overlapping'
    return result


print(better_call_saul())
