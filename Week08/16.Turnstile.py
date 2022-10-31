"""Python"""


def main():
    """Python"""
    lock_status = True

    text_input = input()
    people_pass = 0
    while text_input != 'END':
        if text_input == 'END':
            break

        if lock_status == True:
            if text_input == 'C':
                lock_status = False
        else:
            if text_input == 'P':
                people_pass += 1
                lock_status = True

        text_input = input()

    print(people_pass)


main()
