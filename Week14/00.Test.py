"""SMS"""
 
 
def main():
    """beom"""
    inp = int(input())
    llist = ''
    num = {
        2: ["A", "B", "C"],
        3: ["D", "E", "F"],
        4: ["G", "H", "I"],
        5: ["J", "K", "L"],
        6: ["M", "N", "O"],
        7: ["P", "Q", "R", "S"],
        8: ["T", "U", "V"],
        9: ["W", "X", "Y", "Z"]
    }
    for _ in range(0, inp):
        numm = int(input())
        alphabet = int(input())
        if numm == 1:
            llist = llist[:-alphabet]
        else:
            alphabet = alphabet % len(num[alphabet])
            llist += num[numm][alphabet-1]
    if llist == '':
        print("null")
    else:
        print(llist)
main()