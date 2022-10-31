"""Saul Goodman"""

def breaking_bad():
    """Saul Goodman"""
    all_score = float(input())
    highest_score = float(input())

    if highest_score * 2 < all_score:
        lowest = all_score - highest_score*2
    else:
        lowest = 0

    if highest_score - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")

breaking_bad()
