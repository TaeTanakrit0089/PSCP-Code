'''Saul Goodman'''
def huell():
    '''Saul Goodman'''
    otp = input()
    while int(otp):
        all_num = [int(i) for i in otp]
        all_num_nodup = dict.fromkeys(all_num)
        for i in all_num_nodup:
            all_num_nodup[i] = all_num.count(i)
        all_num_nodup = dict(sorted(all_num_nodup.items(), key=lambda l: l[1], reverse=1))
        all_dup = [values for _, values in all_num_nodup.items()]

        condi4 = all_dup.count(2) == 1
        condi6 = all_dup.count(2) == 2 or all_dup.count(3) == 1
        condi8 = all_dup.count(2) == 3 or all_dup.count(3) == 2
        if list(dict.fromkeys(all_dup)) == [1]:
            print('Invalid')
        elif (len(otp) == 4 and condi4) or (len(otp) == 6 and condi6) or (len(otp) == 8 and condi8):
            print('Valid')
        else:
            print('Invalid')

        otp = input()

huell()
