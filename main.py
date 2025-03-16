VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    if not (2 <= len(hand) <= 5):
        raise ValueError("Hand must contain between 2 and 5 cards.")
    
    values = {"Jack": 10, "Queen": 10, "King": 10}
    score = 0
    ace_count = 0
    
    for card in hand:
        if isinstance(card, int):
            score += card
        elif card in values:
            score += values[card]
        elif card == "Ace":
            ace_count += 1
            score += 11
        else:
            raise ValueError("Invalid card value.")
    
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    
    return "Bust" if score > 21 else score


    