import random


deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]*4


def player_set(num):
    return [[] for _ in range(num)]


def shuffle(deck):
    return random.shuffle(deck)


def deal(deck):
    return deck.pop()


players = int(input("Enter the number of Player: "))
player_list = player_set(players+1)


for deal_round in range(2):
    shuffle(deck)
    for player_index in range(len(player_list)):
        player_list[player_index].append(deal(deck))
