# Exercise

import unittest
from Udemy.Modern_Python3_Bootcamp.OOP_deck_of_cards import Deck, Card

# 1. Make use of an assertions
def eat_junk_food(food):
    assert food in ["Pizza",
                    "Sweets",
                    "Ice-cream",
                    "Chocolate"], "Food must be junk food!"
    return f"Nom, I am eating {food}."


print(eat_junk_food("Salad")) # AssetError: Food must be junk food!

# 2. Make use of doctests
def double(values):
    """double the values in a list

    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """

    return [2 * element for element in values]

# 3. Make use of unit tests by testing the Deck of cards exercise
class CardTests(unittest.TestCase):
    """testing the Card class"""
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.value, "A")
        self.assertEqual(self.card.suit, "Hearts")


class DeckTests(unittest.TestCase):
    """testing the Deck class"""
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have card attribute"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)


if __name__ == '__main__':
    unittest.main()
