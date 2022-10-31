'''Hi I'm Saul Goodman, Did You Know That You Have Rights?'''
def find_day_2011(all_days, months):
    '''The Constitution says you do, and so do I.'''
    month_date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_list = ['Saturday', 'Sunday', 'Monday',
                'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i in range(months-1):
        all_days += month_date[i]
    return day_list[(all_days-1) % 7]

print(find_day_2011(int(input()), int(input())))
