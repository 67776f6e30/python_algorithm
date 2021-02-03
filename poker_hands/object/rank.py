class Rank:
    """
    포커 족보를 정의하는 클래스
    """
    def __init__(self, name: str, weight: int, condition):
        self.name: str = name
        self.weight: int = weight
        self.condition = condition

    def check(self, counter):
        return self.condition(counter)

    def __repr__(self):
        return f"Rank('{self.name}','{self.weight}')"


def high_card_resolver(counter):
    for cards in counter.value:
        if len(cards) >= 1:
            return [cards[:1]]
    return []


def one_pair_resolver(counter):
    for cards in counter.value:
        if len(cards) >= 2:
            return [cards[:2]]
    return []


def two_pair_resolver(counter):
    result = [cards[:2] for cards in counter.value if len(cards) >= 2]
    return result if len(result) == 2 else []


def three_kind_resolver(counter):
    for cards in counter.value:
        if len(cards) >= 3:
            return [cards[:3]]
    return []


def straight_resolver(counter):
    start = 0
    length = 0
    for i, cards in enumerate(counter.value):
        if len(cards):
            start = i
            break

    for i in range(start, len(counter.value)):
        if len(counter.value[i]):
            length += 1
        else:
            break
    return counter.value[start:start+5] if length == 5 else []


def flush_resolver(counter):
    for cards in counter.shape:
        if len(cards) == 5:
            return [cards]
    return []


def full_house_resolver(counter):
    result = []
    for cards in counter.value:
        if len(cards) == 3:
            result.append(cards[:3])
            break
    for cards in counter.value:
        if len(cards) == 2:
            result.append(cards[:2])
            break
    return result if len(result) == 2 else []


def four_kind_resolver(counter):
    for cards in counter.value:
        if len(cards) == 4:
            return [cards[:4]]
    return []


def straight_flush_resolver(counter):
    for cards in counter.shape:
        if len(cards) == 5:
            for i in range(1, 5):
                if cards[0].value_weight() != (cards[i].value_weight() + i):
                    return []
            return [cards]
    return []


def royal_flush_resolver(counter):
    for cards in counter.shape:
        if len(cards) == 5 and cards[0].value_weight() == 13:
            for i in range(1, 5):
                if cards[0].value_weight() != (cards[i].value_weight() + i):
                    return []
            return [cards]
    return []


high_card = Rank('High Card', 1, high_card_resolver)
one_pair = Rank('One Pair', 2, one_pair_resolver)
two_pair = Rank('Two Pair', 3, two_pair_resolver)
three_kind = Rank('Three Kind', 4, three_kind_resolver)
straight = Rank('Straight', 5, straight_resolver)
flush = Rank('Flush', 6, flush_resolver)
full_house = Rank('Full House', 7, full_house_resolver)
four_kind = Rank('Four Kind', 8, four_kind_resolver)
straight_flush = Rank('Straight Flush', 9, straight_flush_resolver)
royal_flush = Rank('Royal Flush', 10, royal_flush_resolver)

rank_list = [high_card, one_pair, two_pair,
             three_kind, straight, flush,
             full_house, four_kind, straight_flush, royal_flush]

rank_list.sort(key=lambda r: r.weight, reverse=True)
