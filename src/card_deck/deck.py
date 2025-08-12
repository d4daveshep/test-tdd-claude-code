from typing import List, NamedTuple


class Card(NamedTuple):
    """
    An immutable playing card with rank and suit.

    Represents a single playing card that cannot be modified after creation.
    Uses NamedTuple for natural immutability with modern type hints.

    Args:
        rank: The card rank (A, 2-10, J, Q, K)
        suit: The card suit (Spades, Hearts, Diamonds, Clubs)
    """

    rank: str
    suit: str

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError(f"can't set attribute '{name}'")


class Deck:
    """
    A standard 52-card deck of playing cards.

    Represents a complete deck of playing cards with all standard suits and ranks.
    Each deck contains exactly 52 unique cards (13 ranks × 4 suits).
    Cards are immutable and the deck provides defensive copies to maintain integrity.

    The deck is initialized with all standard playing cards:
    - Suits: Spades, Hearts, Diamonds, Clubs
    - Ranks: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K

    Attributes:
        cards: A defensive copy of the deck's cards as a List[Card]

    Example:
        >>> deck = Deck()
        >>> len(deck)
        52
        >>> deck.cards[0].rank
        'A'
        >>> deck.cards[0].suit
        'Spades'
    """

    def __init__(self) -> None:
        self._cards: List[Card] = []
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for suit in suits:
            for rank in ranks:
                self._cards.append(Card(rank, suit))

    @property
    def cards(self) -> List[Card]:
        return self._cards[:]  # Return a copy

    def __len__(self) -> int:
        return len(self._cards)

    def __str__(self) -> str:
        return f"Deck with {len(self._cards)} cards"

