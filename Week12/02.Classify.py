'''Saul Goodman'''


def classify():
    '''Saul Goodman'''
    goodman = input()
    data, allyears = [], []
    while goodman != 'END':
        temp = [int(goodman[:2]), int(goodman[2:4]), int(goodman[4:])]
        if int(goodman[:2]) not in allyears:
            allyears.append(int(goodman[:2]))
        data.append(temp)
        goodman = input()
    data.sort()
    allyears.sort()
    result = []
    for yearsrun in allyears:
        currentyear = []
        for j in data:
            if j[0] == yearsrun:
                temp1 = [j[1], j[2]]
                currentyear.append(temp1)
        all_faculty = []
        all_faculty_no_dup = []
        for i in currentyear:
            all_faculty.append(i[0])
            if i[0] not in all_faculty_no_dup:
                all_faculty_no_dup.append(i[0])

        # printprocess
        first_line = True
        for i in all_faculty_no_dup:
            count = all_faculty.count(i)
            if first_line:
                block1 = yearsrun
                first_line = False
            else:
                block1 = '--'
            result.append([block1, i, count])

    for i in result:
        print(*i, sep=' ')


classify()
