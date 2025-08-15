import sys

sys.path.append("src/")

import pytest
from card_deck.card import Card


def test_card_creation_succeeds_when_suit_and_rank_provided():
    """Test that a card can be created with a suit and rank."""
    card = Card(suit="Hearts", rank="Ace")

    assert card.suit == "Hearts"
    assert card.rank == "Ace"


def test_card_suit_modification_fails_when_attempting_to_change():
    """Test that attempting to modify card suit raises an AttributeError."""
    card = Card(suit="Hearts", rank="Ace")

    with pytest.raises(AttributeError):
        card.suit = "Spades"


def test_card_rank_modification_fails_when_attempting_to_change():
    """Test that attempting to modify card rank raises an AttributeError."""
    card = Card(suit="Hearts", rank="Ace")

    with pytest.raises(AttributeError):
        card.rank = "King"


def test_card_attribute_deletion_fails_when_attempting_to_delete():
    """Test that attempting to delete card attributes raises an AttributeError."""
    card = Card(suit="Hearts", rank="Ace")

    with pytest.raises(AttributeError):
        del card.suit

    with pytest.raises(AttributeError):
        del card.rank
