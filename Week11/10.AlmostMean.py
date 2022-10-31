'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    num_per = int(input())
    student_id, student_score = [], []
    sum_avg = 0
    for _ in range(num_per):
        temp_in = input().split()
        student_id.append(int(temp_in[0]))
        student_score.append(float(temp_in[1]))
        sum_avg += float(temp_in[1])

    avg = sum_avg / num_per
    score_space = []
    for i in student_score:
        if i < avg:
            score_space.append(avg-i)
        else:
            score_space.append(max(student_score))
    temp = score_space.index(min(score_space))
    print('%d\t%s' % (student_id[temp], student_score[temp]))


main()
