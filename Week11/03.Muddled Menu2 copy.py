'''Saul Goodman'''


def better_call_saul():
    '''Saul Goodman'''
    data, data_rm = [], []
    goodman = input()
    while goodman != 'DONE':
        if goodman == "SOMETHING'S WRONG":
            data = []
        elif goodman == 'CLOSED':
            data = []
            break
        elif "Can't do:" in goodman:
            data_rm += goodman.replace("Can't do:", "").split(',')
        else:
            data.append(goodman.split(' #'))
            
        goodman = input()
    data_rm = [i.strip() for i in data_rm]
    new_data = []
    if data_rm != []:
        for i in range(len(data)):
            for j in data_rm:
                if j not in data[i][0].strip():
                    new_data.append(data[i])
        data = new_data.copy()
    
    data.sort(key=lambda l:l[0])
    data.sort(key=sort_one)
    print(data)

def sort_one(num):
    '''Saul Goodman'''
    return ord(num[1])

better_call_saul()
