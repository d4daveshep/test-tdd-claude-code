"""
Tests for deck creation functionality.

This test suite covers deck creation and initialization for a standard 52-card deck:
- Standard deck creation with 52 cards
- Deck content validation (suits, ranks, card distribution)
- Error conditions for invalid creation parameters
- Edge cases in deck initialization
"""

import sys
from typing import List, Set, Tuple

import pytest

sys.path.append("src")
from card_deck import Card, Deck


class TestDeckCreation:
    """Test deck creation and initialization."""

    def test_create_standard_deck_has_52_cards(self) -> None:
        """
        Test that a standard deck is created with exactly 52 cards.
        Validates the basic deck initialization functionality.
        """
        deck: Deck = Deck()
        assert len(deck) == 52

    def test_create_deck_returns_deck_instance(self) -> None:
        """
        Test that deck creation returns a Deck instance.
        Validates proper object instantiation.
        """
        deck: Deck = Deck()
        assert isinstance(deck, Deck)

    def test_create_deck_with_no_arguments_creates_standard_deck(self) -> None:
        """
        Test that calling Deck() with no arguments creates a standard 52-card deck.
        Validates default initialization behavior.
        """
        deck: Deck = Deck()
        assert len(deck) == 52
        assert deck is not None


class TestDeckContent:
    """Test deck content validation after creation."""

    def test_standard_deck_contains_all_four_suits(self) -> None:
        """
        Test that a standard deck contains all four suits (Spades, Hearts, Diamonds, Clubs).
        Validates that deck generation includes all required suits.
        """
        deck: Deck = Deck()
        cards: List[Card] = deck.cards
        suits: Set[str] = set(card.suit for card in cards)
        expected_suits: Set[str] = {"Spades", "Hearts", "Diamonds", "Clubs"}
        assert suits == expected_suits

    def test_standard_deck_contains_all_thirteen_ranks(self) -> None:
        """
        Test that a standard deck contains all ranks (A, 2-10, J, Q, K).
        Validates that deck generation includes all required ranks.
        """
        deck: Deck = Deck()
        cards: List[Card] = deck.cards
        ranks: Set[str] = set(card.rank for card in cards)
        expected_ranks: Set[str] = {
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        }
        assert ranks == expected_ranks

    def test_standard_deck_has_exactly_13_cards_per_suit(self) -> None:
        """
        Test that each suit has exactly 13 cards in a standard deck.
        Validates proper distribution of cards across suits.
        """
        deck: Deck = Deck()
        cards: List[Card] = deck.cards
        suits: List[str] = ["Spades", "Hearts", "Diamonds", "Clubs"]

        for suit in suits:
            suit_cards: List[Card] = [card for card in cards if card.suit == suit]
            assert len(suit_cards) == 13

    def test_standard_deck_has_exactly_4_cards_per_rank(self) -> None:
        """
        Test that each rank appears exactly 4 times in a standard deck.
        Validates proper distribution of cards across ranks.
        """
        deck: Deck = Deck()
        cards: List[Card] = deck.cards
        ranks: List[str] = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]

        for rank in ranks:
            rank_cards: List[Card] = [card for card in cards if card.rank == rank]
            assert len(rank_cards) == 4

    def test_standard_deck_has_unique_card_combinations(self) -> None:
        """
        Test that all 52 cards in the deck are unique combinations of rank and suit.
        Validates that no duplicate cards exist.
        """
        deck: Deck = Deck()
        cards: List[Card] = deck.cards
        card_combinations: Set[Tuple[str, str]] = set(
            (card.rank, card.suit) for card in cards
        )
        assert len(card_combinations) == 52

    def test_deck_cards_property_returns_list_of_cards(self) -> None:
        """
        Test that the cards property returns a list containing Card objects.
        Validates proper card object creation and storage.
        """
        deck: Deck = Deck()
        cards: List[Card] = deck.cards
        assert isinstance(cards, list)
        assert len(cards) == 52

        card: Card
        for card in cards:
            assert hasattr(card, "rank")
            assert hasattr(card, "suit")


class TestDeckInitializationEdgeCases:
    """Test edge cases and error conditions during deck creation."""

    def test_multiple_deck_creation_produces_identical_content(self) -> None:
        """
        Test that creating multiple decks produces identical card content.
        Validates consistent deck generation.
        """
        deck1: Deck = Deck()
        deck2: Deck = Deck()

        # Both should have same cards (though order may vary in implementation)
        cards1: Set[Tuple[str, str]] = set(
            (card.rank, card.suit) for card in deck1.cards
        )
        cards2: Set[Tuple[str, str]] = set(
            (card.rank, card.suit) for card in deck2.cards
        )
        assert cards1 == cards2

    def test_deck_creation_with_invalid_arguments_raises_error(self) -> None:
        """
        Test that deck creation with invalid arguments raises appropriate error.
        Validates error handling for improper initialization.
        """
        with pytest.raises(TypeError):
            Deck("invalid_argument")  # type: ignore

    def test_deck_creation_with_multiple_arguments_raises_error(self) -> None:
        """
        Test that deck creation with multiple arguments raises appropriate error.
        Validates that only no-argument initialization is supported.
        """
        with pytest.raises(TypeError):
            Deck(52, "standard")  # type: ignore

    def test_deck_creation_is_repeatable(self) -> None:
        """
        Test that deck creation can be performed multiple times without issues.
        Validates robustness of deck creation process.
        """
        decks: List[Deck] = []
        for _ in range(10):
            deck: Deck = Deck()
            decks.append(deck)
            assert len(deck) == 52

        # All decks should be valid and independent
        assert len(decks) == 10
        deck: Deck
        for deck in decks:
            assert isinstance(deck, Deck)
            assert len(deck) == 52


class TestCardObjectValidation:
    """Test that cards created during deck initialization are valid."""

    def test_all_cards_have_valid_suits(self) -> None:
        """
        Test that all cards in the deck have valid suit values.
        Validates card suit assignment during deck creation.
        """
        deck: Deck = Deck()
        valid_suits: Set[str] = {"Spades", "Hearts", "Diamonds", "Clubs"}
        card: Card
        for card in deck.cards:
            assert card.suit in valid_suits

    def test_all_cards_have_valid_ranks(self) -> None:
        """
        Test that all cards in the deck have valid rank values.
        Validates card rank assignment during deck creation.
        """
        deck: Deck = Deck()
        valid_ranks: Set[str] = {
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        }
        card: Card
        for card in deck.cards:
            assert card.rank in valid_ranks

    def test_cards_are_properly_instantiated_objects(self) -> None:
        """
        Test that each card in the deck is a proper Card object instance.
        Validates card object creation during deck initialization.
        """
        deck: Deck = Deck()
        card: Card
        for card in deck.cards:
            assert hasattr(card, "rank")
            assert hasattr(card, "suit")
            assert isinstance(card.rank, str)
            assert isinstance(card.suit, str)

    def test_deck_contains_expected_specific_cards(self) -> None:
        """
        Test that deck contains specific expected cards like Ace of Spades, King of Hearts.
        Validates that standard deck creation includes all expected card combinations.
        """
        deck: Deck = Deck()
        card_tuples: List[Tuple[str, str]] = [
            (card.rank, card.suit) for card in deck.cards
        ]

        # Test for some specific expected cards
        assert ("A", "Spades") in card_tuples  # Ace of Spades
        assert ("K", "Hearts") in card_tuples  # King of Hearts
        assert ("Q", "Diamonds") in card_tuples  # Queen of Diamonds
        assert ("J", "Clubs") in card_tuples  # Jack of Clubs
        assert ("10", "Spades") in card_tuples  # Ten of Spades
        assert ("2", "Hearts") in card_tuples  # Two of Hearts


class TestCardImmutability:
    """Test that individual cards in the deck are immutable."""

    def test_card_rank_cannot_be_modified(self) -> None:
        """
        Test that card rank property cannot be modified after creation.
        Validates immutability of card rank attribute.
        """
        deck: Deck = Deck()
        card: Card = deck.cards[0]
        original_rank: str = card.rank

        # Attempting to modify rank should raise AttributeError
        with pytest.raises(AttributeError):
            card.rank = "X"  # type: ignore

        # Card rank should remain unchanged
        assert card.rank == original_rank

    def test_card_suit_cannot_be_modified(self) -> None:
        """
        Test that card suit property cannot be modified after creation.
        Validates immutability of card suit attribute.
        """
        deck: Deck = Deck()
        card: Card = deck.cards[0]
        original_suit: str = card.suit

        # Attempting to modify suit should raise AttributeError
        with pytest.raises(AttributeError):
            card.suit = "InvalidSuit"  # type: ignore

        # Card suit should remain unchanged
        assert card.suit == original_suit

    def test_card_has_no_settable_attributes(self) -> None:
        """
        Test that cards have no settable attributes beyond rank and suit.
        Validates complete immutability of card objects.
        """
        deck: Deck = Deck()
        card: Card = deck.cards[0]

        # Attempting to add new attributes should raise AttributeError
        with pytest.raises(AttributeError):
            card.new_attribute = "value"  # type: ignore

        with pytest.raises(AttributeError):
            card.value = 10  # type: ignore

    def test_modifying_cards_list_does_not_affect_original_deck(self) -> None:
        """
        Test that modifying the cards list returned by deck.cards doesn't affect the deck.
        Validates that deck.cards returns a copy, not a reference.
        """
        deck: Deck = Deck()
        original_length: int = len(deck)
        cards_copy: List[Card] = deck.cards

        # Modify the copy
        cards_copy.pop()
        cards_copy.append(cards_copy[0])  # Add a duplicate

        # Original deck should be unchanged
        assert len(deck) == original_length
        assert len(deck.cards) == 52

    def test_cards_maintain_immutability_across_deck_operations(self) -> None:
        """
        Test that cards remain immutable even when accessed through different deck instances.
        Validates consistent card immutability behavior.
        """
        deck1: Deck = Deck()
        deck2: Deck = Deck()

        # Get cards from both decks
        card1: Card = deck1.cards[0]
        card2: Card = deck2.cards[0]  # Should be same type of card (A of Spades)

        # Both cards should be immutable
        with pytest.raises(AttributeError):
            card1.rank = "Modified"  # type: ignore

        with pytest.raises(AttributeError):
            card2.suit = "Modified"  # type: ignore

    def test_card_objects_are_frozen_or_readonly(self) -> None:
        """
        Test that card objects are frozen/readonly and cannot be modified in any way.
        Validates comprehensive immutability enforcement.
        """
        deck: Deck = Deck()
        card: Card = deck.cards[0]

        # Try various ways to modify the card
        with pytest.raises(AttributeError):
            setattr(card, "rank", "Modified")

        with pytest.raises(AttributeError):
            setattr(card, "suit", "Modified")

    def test_card_equality_works_with_immutable_cards(self) -> None:
        """
        Test that card equality comparison works correctly with immutable cards.
        Validates that immutability doesn't break comparison operations.
        """
        deck1: Deck = Deck()
        deck2: Deck = Deck()

        # Find Ace of Spades in both decks
        ace_spades_1: Card | None = None
        ace_spades_2: Card | None = None

        for card in deck1.cards:
            if card.rank == "A" and card.suit == "Spades":
                ace_spades_1 = card
                break

        for card in deck2.cards:
            if card.rank == "A" and card.suit == "Spades":
                ace_spades_2 = card
                break

        assert ace_spades_1 is not None
        assert ace_spades_2 is not None

        # Cards with same rank and suit should be equal
        assert ace_spades_1 == ace_spades_2

        # But they should be different object instances
        assert ace_spades_1 is not ace_spades_2


class TestDeckProperties:
    """Test deck properties and attributes after creation."""

    def test_deck_has_cards_property(self) -> None:
        """
        Test that deck has a cards property that provides access to card collection.
        Validates proper property implementation.
        """
        deck: Deck = Deck()
        assert hasattr(deck, "cards")
        cards: List[Card] = deck.cards
        assert isinstance(cards, list)

    def test_deck_supports_len_function(self) -> None:
        """
        Test that deck supports len() function to get card count.
        Validates __len__ method implementation.
        """
        deck: Deck = Deck()
        length: int = len(deck)
        assert length == 52
        assert isinstance(length, int)

    def test_deck_string_representation_is_meaningful(self) -> None:
        """
        Test that deck has a meaningful string representation.
        Validates __str__ or __repr__ method implementation.
        """
        deck: Deck = Deck()
        deck_str: str = str(deck)
        assert isinstance(deck_str, str)
        assert len(deck_str) > 0
        # Should contain some indication of card count or deck information
        assert any(word in deck_str.lower() for word in ["deck", "card", "52"])


class TestDeckCreationConsistency:
    """Test consistency of deck creation across multiple instances."""

    def test_all_standard_decks_have_same_card_distribution(self) -> None:
        """
        Test that all standard decks have identical card distribution.
        Validates consistent generation of standard deck content.
        """
        deck1: Deck = Deck()
        deck2: Deck = Deck()
        deck3: Deck = Deck()

        decks: List[Deck] = [deck1, deck2, deck3]

        # Check that all decks have same suit distribution
        deck: Deck
        for deck in decks:
            suits: List[str] = [card.suit for card in deck.cards]
            suit_counts: dict[str, int] = {}
            suit: str
            for suit in suits:
                suit_counts[suit] = suit_counts.get(suit, 0) + 1

            expected_count: int = 13
            assert suit_counts["Spades"] == expected_count
            assert suit_counts["Hearts"] == expected_count
            assert suit_counts["Diamonds"] == expected_count
            assert suit_counts["Clubs"] == expected_count

    def test_deck_creation_does_not_modify_global_state(self) -> None:
        """
        Test that creating a deck doesn't affect subsequent deck creations.
        Validates that deck creation is stateless and independent.
        """
        deck1: Deck = Deck()
        first_deck_length: int = len(deck1)

        deck2: Deck = Deck()
        second_deck_length: int = len(deck2)

        # Both decks should be identical and unaffected by each other
        assert first_deck_length == second_deck_length == 52
        assert len(deck1) == 52  # First deck unchanged
