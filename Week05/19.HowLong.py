"""Con man Albuquerque"""


def better_call_saul():
    """Saul Goodman"""
    huell = str(int(input()))
    kuby = 0
    for i in huell:
        if i == '-':
            continue
        kuby += 1
        i = i
    print(kuby)


better_call_saul()
