"""KEY"""


def main():
    """KEY"""
    id_card = input()
    condi_1 = 0

    # condition1
    for i in id_card:
        condi_1 += int(i)

    # condition2
    condi_2 = int(id_card[10]+id_card[11]+id_card[12]) * 10

    # condition3
    sum_all = condi_1+condi_2

    if sum_all < 1000:
        sum_all += 1000

    if len(str(sum_all)) > 4:
        sum_all = str(sum_all)
        print(sum_all[1:])
        # sum_all[start:stop:interval]

    else:
        print(sum_all)


main()
