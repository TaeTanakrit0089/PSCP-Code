"""Steve walks warily down the street"""
def another_one_bite_the_dust():
    """With his brim pulled way down low"""
    balance, text = int(input()), input()
    while text != 'END':
        status, transaction = text.split()
        if status == 'D':
            balance += int(transaction)
        else:
            balance -= int(transaction)
            balance = 0 if balance < 0 else balance
        text = input()
    print(balance)


another_one_bite_the_dust()
