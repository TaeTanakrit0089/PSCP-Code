'''Hi, I'm Saul Goodman. Did you know that you have rights?'''
import hashlib


def lwyrup():
    '''The constitution says you do! And so do I.'''
    decode = input()
    encode = hashlib.sha512(decode.encode('utf-8'))
    encode = encode.hexdigest()
    print(encode.upper())


lwyrup()
