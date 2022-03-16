"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

deck = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "K": 10,
    "Q": 10,
    "J": 10,
    "A": 1,
}


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """

    return deck.get(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    elif value_of_card(card_one) > value_of_card(card_two):
        # Function will break if either card is None
        return card_one
    else:
        return card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10;
           'A' = 11 (if already in hand); numerical value otherwise.

    :return: int - value of the upcoming ace card (either 1 or 11).
    """

    match (card_one, card_two):
        case (card_one, "A" | "J" | "Q" | "K" | "10"):
            return 1
        case ("A" | "J" | "Q" | "K" | "10", card_two):
            return 1
        case _:
            hand_value = value_of_card(card_one) + value_of_card(card_two)

            if hand_value > 10:
                return 1
            else:
                return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """

    match (card_one, card_two):
        case ("A", "J" | "Q" | "K" | "10"):
            return True
        case ("J" | "Q" | "K" | "10", "A"):
            return True
        case _:
            return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """

    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    match (card_one, card_two):
        case ("A", "9" | "10" | "J" | "Q" | "K"):
            return True
        case ("9" | "10" | "J" | "Q" | "K", "A"):
            return True
        case _:

            hand_value = value_of_card(card_one) + value_of_card(card_two)

            if hand_value >= 9 and hand_value <= 11:
                return True
            else:
                return False
