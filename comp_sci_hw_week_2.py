import random

suits = ["♠", "♥", "♦", "♣"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
          "J", "Q", "K", "A"]


def cards_deck():
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + " " + suit)
    return deck


def shuffled_deck():
    final_deck = cards_deck()
    random.shuffle(final_deck)
    return final_deck


def deal_card(deck):
    return deck.pop()


def player_hands(deck):
    player_hand = []
    player_hand.append(deal_card(deck))
    player_hand.append(deal_card(deck))
    return player_hand


def dealer_hands(deck):
    dealer_hand = []
    dealer_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))
    return dealer_hand


def card_value(card):
    value = card.split()[0]
    if value in ["J", "Q", "K"]:
        return 10
    elif value == "A":
        return 11
    else:
        return int(value)


def calculate_score(hand):
    score = 0
    aces = 0

    for card in hand:
        score += card_value(card)
        if card.split()[0] == "A":
            aces += 1

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score


def player_turn(player, deck):
    while calculate_score(player) < 21:
        print("\nYour hand:", player)
        print("Your score:", calculate_score(player))

        choice = input("Hit or stand? (h/s): ").lower()

        if choice == "h":
            player.append(deal_card(deck))
        elif choice == "s":
            break
        else:
            print("Please enter h or s.")

    return player


def dealer_turn(dealer, deck):
    while calculate_score(dealer) < 17:
        dealer.append(deal_card(deck))

    return dealer


def determine_winner(player, dealer):
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    if player_score > 21:
        return "Dealer wins! You busted."
    if dealer_score > 21:
        return "You win! Dealer busted."
    if player_score > dealer_score:
        return "You win!"
    if player_score < dealer_score:
        return "Dealer wins!"
    return "It's a tie!"


deck = shuffled_deck()

player = player_hands(deck)
dealer = dealer_hands(deck)

print("===== BLACKJACK =====")
print("\nYour hand:", player)
print("Your score:", calculate_score(player))
print("\nDealer's hand:", dealer[0], "[hidden]")

player_turn(player, deck)

if calculate_score(player) > 21:
    print("\nYou busted!")
else:
    dealer_turn(dealer, deck)

    print("\n===== FINAL =====")
    print("Your hand:", player)
    print("Your score:", calculate_score(player))
    print("Dealer's hand:", dealer)
    print("Dealer's score:", calculate_score(dealer))
    print("\n" + determine_winner(player, dealer))

print("\nCards left:", len(deck))
