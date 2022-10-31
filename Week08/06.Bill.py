'''Bill'''


def main():
    '''Bill'''
    bill = int(input())
    service = (bill*10)/100
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000

    vat = (bill+service)*107/100
    print("%.2f" % (round(vat, 2)))


main()
