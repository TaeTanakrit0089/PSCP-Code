'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def better_call_saul():
    '''The Constitution says you do, and so do I.'''
    hours, minute, angle_p_min = int(input()) % 12, int(input()), 360/60
    angle_min = (minute / 60)*360
    angle_hour = (hours / 12)*360 + angle_min/12

    condi1 = angle_hour >= angle_min
    condi2 = abs(angle_hour-angle_min) < angle_p_min
    print(condi1 and condi2)

better_call_saul()
