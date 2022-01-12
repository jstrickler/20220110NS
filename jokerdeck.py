from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _create_deck(self):
        super()._create_deck()  # search parents
        for rank in '1', '2':
            card = Card(rank, 'JOKER')
            self._cards.append(card)


