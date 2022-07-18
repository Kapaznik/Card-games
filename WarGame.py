import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        if self.suit == 'Hearts':
            self.suit = '♥'
        elif self.suit == 'Diamonds':
            self.suit = '♦'
        elif self.suit == 'Spades':
            self.suit = '♣'
        elif self.suit == 'Clubs':
            self.suit = '♠'

        return f"{self.value}{self.suit}"


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def pop_card(self):
        return self.all_cards.pop()


# player class
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # remove card from deck
    def remove_card(self):
        if len(self.all_cards) != 0:
            return self.all_cards.pop(0)
        else:
            pass

    # add card
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # check if new_cards is list whice mean there are more then 1 card
            self.all_cards.extend(new_cards)
        else:
            # mean new_cards is single card (object)
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


# setting the game
player_one = Player(input("Enter player 1 name: "))
player_two = Player(input("Enter player 2 name: "))

new_deck = Deck()
new_deck.shuffle()

# split the deck between players (26 each)
for x in range(26):
    player_one.add_cards(new_deck.pop_card())
    player_two.add_cards(new_deck.pop_card())

game_on = True
counter = 0

while game_on:
    counter += 1
    if counter > 10000:
        print("Something going wrong with this game..")
        game_on = False
        break

    else:
        print(f"Round number: {counter}")

        # check if any player lost the game
        if len(player_one.all_cards) == 0:
            print(f"{player_two.name} is the winner!")
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print(f"{player_one.name} is the winner!")
            game_on = False
            break

        # start new round
        # format player1 deck
        player_one_cards = [player_one.remove_card()]

        # format player 2 deck
        player_two_cards = [player_two.remove_card()]

        # game logic
        war_on = True

        while war_on:

            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                war_on = False

            # player2 won
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                war_on = False

            else:
                print("We have war!!!")
                print("-----------------------------------------------")
                print(f"It's a {player_one_cards[-1]} Vs. {player_two_cards[-1]}")
                print("-----------------------------------------------")

                if len(player_one.all_cards) < 3:
                    print(f"{player_one.name} can't play!")
                    print(f"{player_two.name} Won!")
                    game_on = False
                    break

                elif len(player_two.all_cards) < 3:
                    print(f"{player_two.name} can't play!")
                    print(f"{player_one.name} Won!")
                    game_on = False
                    break

                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_card())
                        player_two_cards.append(player_two.remove_card())
