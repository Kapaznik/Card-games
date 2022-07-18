import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


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

    def deal_card(self):
        return self.all_cards.pop()

    def show(self):
        for card in self.all_cards:
            print(card)


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def calc_value(self, card):
        if not decision:
            player = 'Player'
        else:
            player = 'Dealer'
        if card.rank == 'Ace':
            card.value = int(input(f"{player} please choose if Ace is 1 or 11"))
            self.value += card.value
        else:
            self.value += values[card.rank]

    def add_card(self, card):
        self.cards.append(card)
        self.calc_value(card)
        return Card.__str__(card)


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


on_table = True
player_chips = Chips()


def place_bet(chips):
    global on_table
    can_bet = False
    while not can_bet:
        try:
            chips.bet = int(input("Place your bet:"))
            if chips.bet < 0:
                raise ValueError
        except ValueError:
            print("Please enter only numbers!")
            continue
        if chips.total <= 0:
            print("Sorry you don't have money to bet")
            on_table = False
            continue
        elif chips.total < chips.bet:
            print(f"Sorry, your balance is {chips.total} and it's not enough")
            continue
        else:
            return chips.bet


def clear():
    print("\n")


def hit(deck, hand):
    hand.add_card(deck.deal_card())
    show_some(player_hand)


def show_some(player):
    dealer_copy = dealer_hand.cards.copy()
    del dealer_copy[0]
    print("\nDealer's Hand:")
    print("<card hidden>")
    print(*dealer_copy, sep='\n')
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print(f"\nTotal player hand: {player_hand.value}")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def check_dealer_win():
    global on_table
    global game_on
    if choice == 's':
        if dealer_hand.value < 21:
            if dealer_hand.value > player_hand.value:
                print("Dealer won the game!")
                player_chips.lose_bet()
                #  player_chips.lose_bet(place_bet(bet))
                show_all(player_hand, dealer_hand)
                clear()
                game_on = False
        else:
            player_chips.win_bet()


def check_status():
    global on_table
    global game_on
    if player_hand.value == 21:
        print("You won the game!")
        player_chips.win_bet()
        show_all(player_hand, dealer_hand)
        clear()
        game_on = False
        return True

    elif player_hand.value >= 22:
        print(f"You lost because you hand is {player_hand.value}")
        player_chips.lose_bet()
        show_all(player_hand, dealer_hand)
        clear()
        game_on = False
        return True

    elif dealer_hand.value >= 22:
        print(f"You won because the dealer hand is {dealer_hand.value}")
        player_chips.win_bet()
        show_all(player_hand, dealer_hand)
        clear()
        game_on = False
        return True


while on_table:
    game_on = True
    decision = False
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    print(f"You have: {player_chips.total} chips to play")
    print("--------------------------------------------------------")
    if player_chips.total > 0:
        bet = place_bet(player_chips)
        print(player_hand.add_card(deck.deal_card()))
        player_hand.add_card(deck.deal_card())
        dealer_hand = Hand()
        decision = True
        print(dealer_hand.add_card(deck.deal_card()))
        dealer_hand.add_card(deck.deal_card())
        show_some(player_hand)
        decision = False

        while game_on:
            if not check_status():
                if not decision:
                    choice = input("Do you want Hit or Stand?\nPress h for hit and s for stand")
                    if choice.lower() == 'h':
                        hit(deck, player_hand)
                        check_dealer_win()
                    elif choice.lower() == 's':
                        decision = True
                        clear()
                        if not check_dealer_win():
                            hit(deck, dealer_hand)
                else:
                    if not check_dealer_win():
                        hit(deck, dealer_hand)
    else:
        print("You don't have enough money to play!")
        break
