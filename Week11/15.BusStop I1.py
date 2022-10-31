'''Saul Goodman'''
 
 
def main():
    '''Saul Goodman'''
    passenger = int(input())
    busstop = int(input())
    in_bus, count = [], 0
    all_input = [input() for i in range(busstop)]
    final_busstop = int((all_input[-1].split())[0])
    for i in range(1, busstop+1):
        temp = all_input[i-1].split()
        current_station = int(temp[0])
        for _ in range(in_bus.count(current_station)):
            in_bus.remove(current_station)
        temp = [int(x) for x in temp[1:]]
        for j in temp:
            if len(in_bus) >= passenger or current_station == final_busstop:
                break
            if j <= current_station or j > final_busstop:
                continue
            in_bus.append(j)
            count += 1
    print(count)
 
 
main()