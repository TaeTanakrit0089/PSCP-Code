"""Tonight I'm gonna have myself a real good time
    I feel alive
    And the world I'll turn it inside out, yeah
    I'm floating around in ecstasy
    So, (don't stop me now)
    (Don't stop me)
    'Cause I'm having a good time, having a good time"""


def dont_stop_me_now():
    """I'm a shooting star leaping through the sky like a tiger
    Defying the laws of gravity
    I'm a racing car passing by like Lady Godiva
    I'm gonna go, go, go, there's no stopping me
    I'm burnin' through the sky, yeah
    200 degrees, that's why they call me Mister Fahrenheit
    I'm travelling at the speed of light
    I wanna make a supersonic man out of you"""

    data = [input() for _ in range(3)]
    info = [check_hori(data), check_verti(data), check_diag(data)]
    for i in info:
        if i[1]:
            print(i[0], 'WIN')
            return
    print('DRAW')


def check_verti(data):
    '''I'm having such a good time
    I'm having a ball
    (Don't stop me now)
    If you wanna have a good time
    Just give me a call
    (Don't stop me now)
    'Cause I'm having a good time
    (Don't stop me now)
    Yes, I'm havin' a good time
    I don't want to stop at all, yeah'''
    data, transpose = [[*i] for i in data], []
    transpose = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    return check_hori(transpose)


def check_hori(data):
    '''I'm a rocket ship on my way to Mars on a collision course
    I am a satellite I'm out of control
    I am a sex machine ready to reload like an atom bomb
    About to oh, oh, oh, oh, oh, explode
    I'm burnin' through the sky, yeah
    200 degrees, that's why they call me Mister Fahrenheit
    I'm travelling at the speed of light
    I wanna make a supersonic woman of you'''
    for i in data:
        temp = set([*i])
        if len(temp) == 1 and temp != {'-'}:
            return (*temp, True)
    return ('', False)


def check_diag(data):
    '''Hey, hey, hey
    (Don't stop me, don't stop me, ooh, ooh, ooh) I like it
    (Don't stop me, don't stop me) Have a good time, good time
    (Don't stop me, don't stop me) Woah
    Let loose, honey, all right
    Oh, I'm burnin' through the sky, yeah
    200 degrees, that's why they call me Mister Fahrenheit (hey)
    I'm travelling at the speed of light
    I wanna make a supersonic man out of you (hey, hey)'''
    left, right = [], []
    for i in range(3):
        for j in range(3):
            left += [data[i][j]] if i == j else []
            right += [data[i][j]] if i+j == 2 else []
    return check_hori([left, right])


dont_stop_me_now()
