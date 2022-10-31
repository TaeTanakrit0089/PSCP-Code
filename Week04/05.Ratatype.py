'''Saul Goodman'''


def main():
    '''Saul Goodman'''
    word1_1 = """In Deep Learning, a Convolutional Neural Network (CNN) is a class of """
    word1_2 = """Deep Neural Networks, most commonly applied to analyzing visual imagery."""
    word2_1 = """"Two things are infinite: the universe and human stupidity; and I'm not """
    word2_2 = """sure about the universe". - Albert Einstein"""
    word3_1 = """Statistics is the discipline that concerns the collection, organization, """
    word3_2 = """displaying, analysis, interpretation and presentation of data."""
    word4_1 = "The backslash (\\) is a typographical mark used mainly in computing and "
    word4_2 = \
    """is the mirror image of the common slash (/). It is sometimes called "escape character"."""

    num1 = int(input())
    if num1 == 1:
        print(word1_1+word1_2)
    elif num1 == 2:
        print(word2_1+word2_2)
    elif num1 == 3:
        print(word3_1+word3_2)
    elif num1 == 4:
        print(word4_1+word4_2)


main()
