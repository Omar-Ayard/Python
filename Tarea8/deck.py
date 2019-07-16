from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:

    def __init__(self):
        suits=["Heart", "Diamond", "Clubs", "Spades"]
        values=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []

        for suit in suits:
            for value in values:
              self.cards.append(Card(suit,value))

    def __repr__(self):
        return f'Deck of {self.count()} Cards'

    def count(self):
        return len(self.cards)

    def _deal(self,number):
        hand = []
        if self.count() > 0:
            if number > self.count():
                number=self.count()
            for ind in range(number):
                hand.append(self.cards.pop())
        else:
            raise ValueError('All cards have been dealt')

        return hand

    def deal_hand(self,number):
        return self._deal(number)

    def deal_card(self):
        return self._deal(1)

    def shuffle(self):
        if self.count() == 52:
            shuffle(self.cards)
            return self.cards
        else:
            raise ValueError('Only full decks can be shuffled')

if __name__ == "__main__":
    myDeck = Deck()
    print("We have: "+str(myDeck.count())+" in the Deck")
    print(f'Initial Deck: {myDeck.cards}')

    try:
        print(myDeck.deal_card())
        print(myDeck.count())
        print(myDeck.deal_hand(10))
        print(myDeck.count())
        print(myDeck.deal_hand(52))
        print(myDeck.count())
        print(myDeck.deal_hand(3))
        print(myDeck.count())
        print(f'After Deal {myDeck.cards}')
    except ValueError as err:
        print(err)

    #print(f'Shuffle: {myDeck.shuffle()}')
    #print(f'Original: {myDeck.cards}')
