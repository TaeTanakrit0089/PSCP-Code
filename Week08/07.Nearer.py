'''l'''


def main():
    '''ice cream'''
    alice = int(input())
    bob = int(input())
    ice_cream = int(input())

    distance_alice = abs(alice - ice_cream)
    distance_bob = abs(bob - ice_cream)

    if distance_alice < distance_bob:
        print("Alice %d" % distance_alice)
    elif distance_bob < distance_alice:
        print("Bob %d" % distance_bob)
    else:
        print("Sundaes %d" % min(distance_alice, distance_bob))


main()
