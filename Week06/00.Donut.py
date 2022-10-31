"""donut"""
def main():
    """input"""
    pricedonut = int(input())
    promo = int(input())
    getfree = int(input())
    buy = int(input())
    free = buy // promo
    print(pricedonut * (promo - getfree), free)
main()
