value_weight = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    '10': 9,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

shape_weight = {
    'C': 1,
    'D': 2,
    'H': 3,
    'S': 4
}


class Card:
    """
    포커 카드를 정의하는 클래스
    """
    def __init__(self, card_text: str):
        self.value = card_text[:-1]
        self.shape = card_text[-1]

    def weight(self):
        return value_weight[self.value], shape_weight[self.shape]

    def value_weight(self):
        return value_weight[self.value]

    def shape_weight(self):
        return shape_weight[self.shape]

    def __lt__(self, other):
        if isinstance(other, Card):
            return self.weight() < other.weight()
        return self.weight() < other

    def __le__(self, other):
        if isinstance(other, Card):
            return self.weight() <= other.weight()
        return self.weight() <= other

    def __gt__(self, other):
        if isinstance(other, Card):
            return self.weight() > other.weight()
        return self.weight() > other

    def __ge__(self, other):
        if isinstance(other, Card):
            return self.weight() >= other.weight()
        return self.weight() >= other

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.weight() == other.weight()
        return self.weight() == other

    def __repr__(self):
        return f'Card({self.value + self.shape!r})'
