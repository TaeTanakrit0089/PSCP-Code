"""pscp"""
import time
 
def my_main():
    """lab-10"""
    get_num = int(input())
    global start_time
    start_time = time.time()
    count = len(str(get_num))
    count_1 = 1
    count_9 = 9
    tap_num = 0
    
    if get_num == 1:
        print(1)
        quit()
    for i in range(1, count):
        howmany = (count_9 - count_1)+1
        tap_num += howmany * i
        count_1 = int(str(count_1) + "0")
        count_9 = int(str(count_9) + "9")
 
    last_count = ((get_num - count_1) + 1) * count
    total = (tap_num + last_count) + get_num
    print(total)
 
my_main()
print("Process finished --- %f seconds ---" % (time.time() - start_time))
