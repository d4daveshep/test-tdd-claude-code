from typing import NamedTuple


class Card(NamedTuple):
    """An immutable playing card with a suit and rank."""
    suit: str
    rank: str

