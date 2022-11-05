"BreachTheDoor"
def main():
    "IAM503ROT8OOSS001LKFD"
    txt = input() + ' '
    txt_list = []
    txt_tst = ""
    pass_list = []
    for i in txt:
        if i.isalpha():
            txt_tst += i
        else:
            if txt_tst != "":
                txt_list.append(txt_tst)
                txt_tst = ""
    for i in txt_list:
        if len(i) > 6:
            pass_list.append(i)
    print(*pass_list)
main()