'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    room_area, room_height, all_guys = int(input()), int(input()), int(input())
    room_type, room_d = input(), input()

    btu = cal_btu(room_area)
    temp1 = (max(8, room_height) - 8) * 1000
    temp2 = (max(2, all_guys) - 2) * 600
    temp3 = 4000 if room_type == 'kitchen' else 0
    btu += temp1 + temp2 + temp3

    temp4 = btu*0.1*-1 if room_d == 'shaded' else btu*0.1 if room_d == 'facing the sun' else 0
    return btu + temp4


def cal_btu(area):
    '''Saul Goodman'''
    data = {2000: 34, 1500: 30, 1400: 24, 1200: 23, 1000: 21, 700: 18, 550: 14, 450: 12,
            400: 10, 350: 9, 300: 8, 250: 7, 150: 6}
    for i, j in data.items():
        if area > i:
            return j*1000
    return 5000


print(round(better_call_saul()))
