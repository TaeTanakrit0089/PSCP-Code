"""IG: few.pz"""
import hashlib


def password(decode):
    '''The constitution says you do! And so do I.'''
    encode = hashlib.sha512(decode.encode('utf-8'))
    encode = encode.hexdigest()
    return encode.upper()


def main():
    """ Main function """
    encrypted = input()
    for i in range(100000):
        if password(str('%05d' % i)) == encrypted:
            print('%05d' % i)
            break


main()
