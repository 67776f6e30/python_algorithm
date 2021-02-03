from collections import defaultdict
from object.game import Game
from object.player import Player


def main():
    result = defaultdict(int)

    with open('poker.txt', 'r') as file:
        data = [line for line in file]

    player_1 = Player(1, 'Player 1')
    player_2 = Player(2, 'Player 2')

    game = Game([player_1, player_2])

    for line in data:
        cards = line.strip().split(' ')
        player_1.hands.set_hands(cards[:5])
        player_2.hands.set_hands(cards[5:])
        result[game.winner_check()] += 1

    print(f"{player_1.name}'s Win Count : {result[player_1.name]}")


if __name__ == '__main__':
    main()
