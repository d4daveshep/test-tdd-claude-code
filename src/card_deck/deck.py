from typing import List

class Card:
    __slots__ = ('_rank', '_suit')
    
    def __init__(self, rank: str, suit: str) -> None:
        object.__setattr__(self, '_rank', rank)
        object.__setattr__(self, '_suit', suit)
    
    @property
    def rank(self) -> str:
        return self._rank
    
    @property
    def suit(self) -> str:
        return self._suit
    
    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError(f"can't set attribute")
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank and self.suit == other.suit
    
    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

class Deck:
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