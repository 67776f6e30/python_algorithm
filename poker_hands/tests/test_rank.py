from unittest import TestCase, main
from ..object.card import Card
from ..object.hands import Hands
from ..object.rank import rank_list, high_card, one_pair, two_pair, \
    three_kind, straight, flush, full_house, four_kind, \
    straight_flush, royal_flush


class RankTest(TestCase):
    """
    포커 족보의 조건을 체크하는 테스트 클래스
    """
    @classmethod
    def setUpClass(cls) -> None:
        cls.hands = Hands()

    def get_cards(self, text_list):
        return sorted([sorted([Card(t) for t in text.split(' ')], reverse=True)
                       for text in text_list if len(text)], reverse=True)

    def cards(self, text):
        return sorted([Card(t) for t in text.split(' ')], reverse=True) \
            if text else []

    def flat(self, cards_list):
        return [card for cards in cards_list for card in cards]

    def test_high_card(self):
        data_set = [
            ('JS KD 3C 6S 4S', 'KD'),
            ('7C AH QC KS 5H', 'AH'),
            ('TD AD 6S KH KD', 'AD'),
            ('AS 7S 5S TS 9S', 'AS'),
            ('4S 4H 4C 4C JS', 'JS')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(high_card.check(self.hands.count)))

    def test_one_pair(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('7C 7H QC KS 5H', '7C 7H'),
            ('TD AD KS KH KD', 'KH KS'),
            ('AS AC AH AD 9S', 'AS AH'),
            ('4S 4H 4C 5C 5S', '5S 5C')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(one_pair.check(self.hands.count)))

    def test_two_pair(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('7C 7H QC KS 5H', ''),
            ('TD TS KS KH KD', 'KH KS TD TS'),
            ('AS AC AH AD 9S', ''),
            ('4S 4H 3C 5C 5S', '5S 5C 4S 4H')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(two_pair.check(self.hands.count)))

    def test_three_kind(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('7C 7H QC KS 5H', ''),
            ('TD TS KS KH KD', 'KH KS KD'),
            ('AS AC AH AD 9S', 'AS AH AD'),
            ('4S 4H 3C 5C 5S', '')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(three_kind.check(self.hands.count)))

    def test_straight(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('5C 6H 7C 8S 9H', '5C 6H 7C 8S 9H'),
            ('AD KS QS JH TD', 'AD KS QS JH TD'),
            ('QS KC AH 2D 3S', ''),
            #('AS 2H 3C 4C 5S', 'AS 2H 3C 4C 5S')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(straight.check(self.hands.count)))

    def test_flush(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('7C 7H QC KS 5H', ''),
            ('TD TS KS KH KD', ''),
            ('AS AC AH AD 9S', ''),
            ('4S 2S 3S 5S 9S', '4S 2S 3S 5S 9S')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(flush.check(self.hands.count)))

    def test_full_house(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('7C 7H QC KS 5H', ''),
            ('TD TS KS KH KD', 'KS KH KD TS TD'),
            ('AS AC AH AD 9S', ''),
            ('TS 2S 3S TD TH', '')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(full_house.check(self.hands.count)))

    def test_four_kind(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('7C 7H QC KS 5H', ''),
            ('KC TS KS KH KD', 'KH KS KD KC'),
            ('AS AC AH AD 9S', 'AS AH AD AC'),
            ('4S 4H 3C 5C 5S', '')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(four_kind.check(self.hands.count)))

    def test_straight_flush(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('5C 6H 7C 8S 9H', ''),
            ('AS KS QS JS TS', 'AS KS QS JS TS'),
            ('QS KC AH 2D 3S', ''),
            ('AS 2H 3C 4C 5S', '')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(straight_flush.check(self.hands.count)))

    def test_royal_flush(self):
        data_set = [
            ('JS KD 3C 6S 4S', ''),
            ('5C 6C 7C 8C 9C', ''),
            ('AS KS QS JS TS', 'AS KS QS JS TS'),
            ('QS KC AH 2D 3S', ''),
            ('AS 2H 3C 4C 5S', '')
        ]
        for data in data_set:
            with self.subTest():
                self.hands.set_hands(data[0].split(' '))
                self.assertEqual(self.cards(data[1]),
                                 self.flat(royal_flush.check(self.hands.count)))


if __name__ == '__main__':
    main()
