'''prepro'''


def main():
    '''Prepro'''
    text = []
    parade = input()

    while parade != "END":
        text += parade.split(', ')
        parade = input()

    # remove dog
    for _ in range(text.count("IT'S A DOG")):
        dog_index = text.index("IT'S A DOG")
        del text[dog_index-1], text[dog_index-1]
    all_species = dict.fromkeys(text)
    all_spicies_sorted = sorted(list(all_species))
    for key, _ in all_species.items():
        all_species.update({key: text.count(key)})

    # final print
    for i in all_spicies_sorted:
        first_seen = text.index(i) + 1
        number = all_species[i]
        print('%s %d %d' % (i, first_seen, number))


main()
