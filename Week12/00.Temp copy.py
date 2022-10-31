"""Saul Goodman"""
def main():
    """Saul Goodman"""
    data = {1: 'AEILNORSTU', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5:
            'K', 8: 'JX', 10:'QZ'}
    word_test, score = input(), 0
    for keys, values in data.items():
        for i in word_test:
            if i in values:
                score += keys
    print(score)
main()
