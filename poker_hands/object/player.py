from .hands import Hands


class Player:
    """
    포커 플레이어의 정보를 저장
    """
    def __init__(self, id: int, name: str):
        self.id = id
        self.name: str = name
        self.hands: Hands = Hands()

    def __repr__(self):
        return f"Player({self.id!r}, {self.name!r}, {self.hands!r})"
