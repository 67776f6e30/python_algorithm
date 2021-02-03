from .card import Card


class HandsCounter:
    """
    포커 카드를 종류별로 카운트하는 클래스
    """
    def __init__(self):
        self.value_list = 'AKQJT98765432' + '0'
        self.shape_list = 'SHDC' + '0'
        self.value = [[] for _ in self.value_list]
        self.shape = [[] for _ in self.shape_list]

    def reset(self):
        self.value = [[] for _ in self.value_list]
        self.shape = [[] for _ in self.shape_list]

    def sort(self):
        for v in self.value:
            v.sort(reverse=True)
        for s in self.shape:
            s.sort(reverse=True)

    def set_card(self, cards: list[Card]):
        for card in cards:
            self.value[len(self.value_list) - card.value_weight()].append(card)
            self.shape[len(self.shape_list) - card.shape_weight()].append(card)
        self.sort()

    def __len__(self):
        return self.length


class Hands:
    """
    포커 카드의 집합을 관리하는 클래스
    """
    def __init__(self):
        self.cards = []
        self.count = HandsCounter()

    def set_hands(self, cards):
        self.count.reset()
        self.cards = [Card(text) for text in cards]
        self.count.set_card(self.cards)

    def __str__(self):
        return ' '.join(self.cards)

    def __repr__(self):
        return f'Hands({self.cards!r})'
