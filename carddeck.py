import random


class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    # to-string method (human friendly)
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    # code friendly
    def __repr__(self):
        # represent the object in Python code
        return f"Card('{self.rank}', '{self.suit}')"



class CardDeck:  # object
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    # constructor
    def __init__(self, dealer):
        # private variable
        self._dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    # instance method
    def shuffle(self):
        random.shuffle(self._cards)

    # instance method
    def deal(self):
        return self._cards.pop()


    @property
    def cards(self):
        return self._cards


    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")


# self._dealer   private variable
# self.dealer public variable
#       (AKA property)




