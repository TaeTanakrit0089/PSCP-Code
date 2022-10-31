'''Want to crack into somebody's safe? Better Call Saul! He knows a guy who knows a guy
who can crack anything in this world!'''

def better_call_saul(text_from, text_to, summer=0):
    '''I woke up I found her that all I know'''
    for i in range(len(text_from)):
        alphafrom, alphato = ord(text_from[i]), ord(text_to[i])
        temp1 = abs(alphato-alphafrom)
        temp2 = 26 - temp1
        summer += min(temp1, temp2)
    return summer

print(better_call_saul(input(), input()))
