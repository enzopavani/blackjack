import random

def deal_card(player_hand):
    card = random.choice(cards)
    if card == 11:
        if card_sum(player_hand) + 11 > 21:
            card = 1
    player_hand.append(card)

def start_game():
    for _ in range(2):
        deal_card(user_hand)
        deal_card(pc_hand)

def card_sum(player_hand):
    card_sum = 0
    for card in player_hand:
        card_sum += card
    return card_sum

def has_bj(player_hand):
    if card_sum(player_hand) == 21:
        return True
    return False


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
user_score = 0
pc_hand = []
pc_score = 0

start_game()
player_turn = True
game_end = False
while not game_end:
    while player_turn:
        user_score = card_sum(user_hand)
        pc_score = card_sum(pc_hand)
        if has_bj(pc_hand) or has_bj(user_hand) or user_score > 21:
            player_turn = False
            game_end = True
        else:
            print(f"User - {user_hand}\tscore - {user_score}")
            print(f"PC - [{pc_hand[0]}]")
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                deal_card(user_hand)
            else:
                player_turn = False
    while pc_score < 16 and not game_end:
        deal_card(pc_hand)
        pc_score = card_sum(pc_hand)
    print(f"\nPlayer hand = {user_hand}\tscore = {user_score}")
    print(f"PC hand = {pc_hand}\tscore = {pc_score}")
    if pc_score == 21 and len(pc_hand) == 2:
        print("\nPC won (Blackjack).")
        game_end = True
    elif user_score == 21 and len(user_hand) == 2:
        print("\nYou won (Blackjack).")
        game_end = True
    elif user_score > 21:
        print("\nPC won (User over 21 points)")
    elif pc_score > 21:
        print("\nYou won (PC over 21 points).")
        game_end = True
    elif pc_score > user_score:
        print("\nYou lose (PC has more points).")
        game_end = True
    elif pc_score < user_score:
        print("\nYou won (User has more points).")
        game_end = True
    else:
        print("\nIt's a draw (User tied the PC).")
        game_end = True


