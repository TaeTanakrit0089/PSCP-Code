'''Saul Goodman'''


from math import floor


def main():
    '''Saul Goodman'''
    command = input()
    input()
    address = input()
    attemp1, attemp2, attemp3, attemp4 = input(), input(), input(), input()
    # first output line
    first_address = find_url(command, 1)
    if first_address:
        ip_address = remove_colon(find_url(command, 2))
    else:
        web_url = remove_colon(find_url(command, 2))
        ip_address = find_ip_from_secondline(address, web_url)

    # second output line
    error_code = count_error(attemp1, attemp2, attemp3, attemp4)
    error_cal = calculate_error(error_code)
    l2_receive = float(error_cal[0])
    l2_lost = float(error_cal[2])
    l2_percent = float(error_cal[4:])

    # forth output line
    nmin = find_time(attemp1, attemp2, attemp3, attemp4, 1)
    nmax = find_time(attemp1, attemp2, attemp3, attemp4, 2)
    navg = find_time(attemp1, attemp2, attemp3, attemp4, 3)

    # print all
    print('Ping statistics for %s:' % ip_address)
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%d%% loss),' %
          (l2_receive, l2_lost, l2_percent))
    if l2_percent == 100:
        return 0
    print('Approximate round trip times in milli-seconds:')
    print('    Minimum = %dms, Maximum = %dms, Average = %dms' %
          (nmin, nmax, navg))
    # print(error_cal)


def remove_colon(text1):
    '''Remove Colon'''
    temp = ''
    for i in text1:
        condi1 = i == '.' or i == ':' or i == '/'
        condi2 = i.isnumeric() or i.isalpha()
        if condi1 or condi2:
            temp += i
    return temp


def find_url(command, state):
    '''Saul Goodman'''
    ping_located = command.index('ping') + 5
    command_cut = command[ping_located:].strip()

    if state == 1:
        if command_cut[0].isnumeric():
            return True
        else:
            return False
    else:
        return str(command_cut)


def find_ip_from_secondline(command, web_url):
    '''Saul Goodman'''
    url_located = command.index('[')

    command_cut = command[url_located:].replace(web_url, '').strip()
    space_located = command_cut.index(' ')
    command_cut = command_cut[:space_located].replace('[', '').replace(']', '')
    return str(command_cut)


def find_ip_from_secondline2(command, web_url):
    '''Saul Goodman'''
    web_url = web_url.replace('www.', '')
    url_located = command.index(web_url)

    command_cut = command[url_located:].replace(web_url, '').strip()
    space_located = command_cut.index(' ')
    command_cut = command_cut[:space_located].replace('[', '').replace(']', '')
    return str(command_cut)


def count_error(line1, line2, line3, line4):
    '''Count Error From Line 2 in format of xxxx'''
    first_format = 'Reply from'
    final_code = ''
    if line1[:10] == first_format:
        final_code += '0'
    else:
        final_code += '1'

    if line2[:10] == first_format:
        final_code += '0'
    else:
        final_code += '1'

    if line3[:10] == first_format:
        final_code += '0'
    else:
        final_code += '1'

    if line4[:10] == first_format:
        final_code += '0'
    else:
        final_code += '1'

    return str(final_code)


def calculate_error(errorcode):
    '''calculate error from line 2'''
    all_error = 0
    all_success = 4
    for i in errorcode:
        if i == '1':
            all_error += 1
            all_success -= 1

    percent_loss = all_error / 4 * 100
    return_result = str(round(all_success))[0]+','+str(round(all_error))[0] + \
        ','+str(round(percent_loss))
    return return_result


def find_time(line1, line2, line3, line4, return_val):
    '''find time'''
    time_all = ''
    time1 = sub_find_time(line1)
    time2 = sub_find_time(line2)
    time3 = sub_find_time(line3)
    time4 = sub_find_time(line4)
    time_all += time1+','+time2+','+time3+','+time4

    # find average
    count = 0
    sum_all = 0
    temp = ''
    time_without_zero = ''
    haszero = False
    time_all_avg = time_all + ','
    for i in time_all_avg:
        if i.isnumeric():
            temp += str(i)
        else:
            if int(temp) != 0:
                time_without_zero += temp + ','
            temp = int(temp)
            sum_all += temp
            if temp == 0:
                haszero = True
                temp = ''
                continue
            temp = ''
            count += 1
    if sum_all == 0 and count == 0:
        avg = 0
    else:
        avg = floor(sum_all/count)
    if not haszero:
        time_without_zero = time_all+','

    temp = ''
    # find max
    nmax = 0
    for i in time_without_zero:
        if i == ',':
            num1 = int(temp)
            if num1 > nmax:
                nmax = num1
            temp = ''
        else:
            temp += i

    # find min
    if avg == 0:
        nmin = 0
    else:
        nmin = 999999
    temp = ''
    for i in time_without_zero:
        if i == ',':
            num1 = int(temp)
            if num1 < nmin:
                nmin = num1
            temp = ''
        else:
            temp += i

    if return_val == 1:
        return nmin
    elif return_val == 2:
        return nmax
    elif return_val == 3:
        return avg


def sub_find_time(line):
    '''find time'''
    condi1 = line[:10] == 'Reply from'
    if not condi1:
        return str(0)
    time_symbol_index = line.index('time')+4
    time_symbol = line[time_symbol_index]
    if time_symbol == '<':
        return str(0)
    time_cut = line[time_symbol_index:].replace('=', '')
    time_spread = ''
    for i in time_cut:
        if i.isalpha():
            break
        time_spread += i

    return str(time_spread)


main()
