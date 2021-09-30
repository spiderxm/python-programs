from random import shuffle

suite = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


# my_cards = [(s,r) for s in suite for r in ranks]
# my_cards=[]
# for r in ranks:
#     for s in suite:
#         my_cards.append((s,r))


class Deck:
    """
    This is the deck class. This object will create a deck of cards to initiate the game.

    """

    def __init__(self):
        print('Creating New Ordered deck')
        self.all_cards = [(s, r) for s in suite for r in ranks]

    def shuffle(self):
        print('shuffling the deck')
        shuffle(self.all_cards)

    def split_in_half(self):
        return self.all_cards[:26], self.all_cards[26:]


class Hand:
    """
    This is the hand class. Each player has a hand, and can add or remove cards form that hand.
    """

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
     Player class
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        returns true if player still has cards
        """
        return len(self.hand.cards) != 0


# Game Play
print("Welcome to War game, let's begin  ")

# create new deck and split it in half

d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# create players
comp = Player("Computer", Hand(half1))
name = input("Your Name")
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for new round")
    print("Current standing")
    print(user.name + "has the count: " + str(len(user.hand.cards)))
    print(comp.name + "has the count: " + str(len(comp.hand.cards)))
    print("Play a card!")
    print('\n')

    table_cards =[]
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1
        print("war")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print("Game over, number of rounds: " + str(total_rounds))
print("War happened: " + str(war_count) + "times")
print(user.name + " still has cards? >>>  ", str(user.still_has_cards()))
print("Computer still has cards? >>>  ", str(comp.still_has_cards()))

