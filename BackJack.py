import random

deck: list[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4


def shuffle_deck() -> None:

    random.shuffle(deck)


def deal_card() -> str:

    return deck.pop()


def show_hand(computer_hand: list[str], player_hand: list[str]) -> None:

    computer_shown_hand = str(
        [computer_hand[0]] + ["?" for _ in range(len(computer_hand) - 1)]
    )
    player_shown_hand = str(player_hand)

    print(f"Computer's hand: {computer_shown_hand:>21}")
    print(f"Player's hand: {player_shown_hand:>23}")


def get_value(hand: list[str]) -> int:

    cards_value: int = 0

    # swaps [0] and [1] if 'A' is at [0]
    if hand[0] == "A":
        hand[0] = hand[1]
        hand[1] = "A"

    # converts str to int
    for card in hand:
        if not card in ["J", "Q", "K", "A"]:
            cards_value += int(card)
        elif card in ["J", "Q", "K"]:
            cards_value += 10
        else:
            if cards_value + 11 <= 21:
                cards_value += 11
            else:
                cards_value += 1

    return cards_value


def check_player_draw_card() -> bool:

    player_input = input("Draw Card? (y/n): ")

    while True:
        if player_input in ["y", "Y"]:
            return True
        elif player_input in ["n", "N"]:
            return False
        else:
            player_input = input("Draw Card? (y/n): ")


def check_computer_draw_card(computer_hand: list[str]) -> bool:

    # arguments for random.choices
    true_prob: float = 0.0
    false_prob: float = 0.0
    value: list[bool] = [True, False]
    prob: list[float] = [true_prob, false_prob]
    # counts cards' value for calculating prob
    cards_value: int = get_value(computer_hand)

    # print(f"{computer_hand}: {cards_value}")

    true_prob = (21 - cards_value) / len(deck)
    false_prob = 1 - true_prob
    if true_prob < 0:
        true_prob = 0
        false_prob = 1

    prob = [true_prob, false_prob]

    # print(value, prob)

    return random.choices(value, prob)[0]


def show_winner(computer_hand: list[str], player_hand: list[str]) -> None:

    computer_value: int = get_value(computer_hand)
    player_value: int = get_value(player_hand)

    print("--------------------------------------")

    print(f"Computer's hand: {f'{computer_hand} = {computer_value}':>21}")
    print(f"Player's hand: {f'{player_hand} = {player_value}':>23}")

    if computer_value > player_value or computer_value == 21:
        print("Computer wins")
    elif player_value > 21:
        print("Player exploded, Computer wins")
    else:
        print("Player wins")


def main():

    # initialise list to store cards for player and computer
    player_hand: list[str] = []
    computer_hand: list[str] = []

    # 'Game Start' headline, and shuffle deck
    print("==============GAME START==============")
    shuffle_deck()

    # deals 2 cards for both
    for _ in range(2):
        computer_hand.append(deal_card())
        player_hand.append(deal_card())

    # shows first card of computer, and both cards of player
    show_hand(computer_hand, player_hand)

    while check_player_draw_card():
        player_hand.append(deal_card())

        # shows first card of computer, and both cards of player
        show_hand(computer_hand, player_hand)

    if check_computer_draw_card(computer_hand):
        computer_hand.append(deal_card())
        show_hand(computer_hand, player_hand)

    show_winner(computer_hand, player_hand)


if __name__ == "__main__":
    main()
