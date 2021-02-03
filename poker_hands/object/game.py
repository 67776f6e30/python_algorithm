from .player import Player
from .rank import rank_list


class Game:
    """
    포커 게임을 관리하는 클래스
    """
    def __init__(self, players: list[Player]):
        self.players: list[Player] = players

    def winner_check(self):
        result = []
        for player in self.players:
            for rank in rank_list:
                if cards := rank.check(player.hands.count):
                    result.append((rank.weight, cards, player))
                    break

        return sorted(result, reverse=True)[0][2].name
