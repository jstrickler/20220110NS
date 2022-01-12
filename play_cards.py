from carddeck import CardDeck, Card
from jokerdeck import JokerDeck

d1 = CardDeck("Nellie")
d2 = CardDeck("Andy")

print(d1, d2)

# BAD
# print(d1._dealer)

print(d1.dealer)  # getter property
print(d2.dealer)

# d1._dealer = "Bob"  # NAUGHTY!!
# print(d1.dealer)

d1.dealer = "Little Bear"   # setter property

print(d1.dealer)

try:
    d1.dealer = 123.456
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

c = Card('2', 'Clubs')
print(c.suit, c.rank, c, repr(c))

d1.shuffle()
print(d1.cards)

for _ in range(5):
    c = d1.deal()
    print(c)
print()
print('-' * 60)

j1 = JokerDeck("Bonnie")
print(j1)
j1.shuffle()
print(j1.cards)
