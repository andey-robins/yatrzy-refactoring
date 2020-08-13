class Hand:
    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5


class Scoring:
    @staticmethod
    def ones(hand):
        return single_number(hand, 1)

    @staticmethod
    def twos(hand):
        return single_number(hand, 2)

    @staticmethod
    def threes(hand):
        return single_number(hand, 3)

    @staticmethod
    def fours(hand):
        return single_number(hand, 4)

    @staticmethod
    def fives(hand):
        return single_number(hand, 5)

    @staticmethod
    def sixes(hand):
        return single_number(hand, 6)

    @staticmethod
    def chance(hand):
        return sum(hand.dice)

    @staticmethod
    def yatzy(hand):
        firstDie = hand.dice[0]
        for i in range(1, len(hand.dice)):
            if hand.dice[i] != firstDie:
                return 0
        return 50

    @staticmethod
    def pair(hand):
        counts = dict.fromkeys(range(1, 7), 0)
        for die in hand.dice:
            counts[die] += 1

        for location in reversed(range(1, 7)):
            if counts[location] >= 2:
                return location * 2
        return 0

    @staticmethod
    def two_pair(hand):
        counts = dict.fromkeys(range(1, 7), 0)
        for die in hand.dice:
            counts[die] += 1

        pairs = 0
        score = 0

        for location in reversed(range(1, 7)):
            if counts[location] >= 2:
                pairs += 1
                score += location * 2

        if pairs == 2:
            return score
        else:
            return 0

    @staticmethod
    def three_of_a_kind(hand):
        counts = dict.fromkeys(range(1, 7), 0)
        for die in hand.dice:
            counts[die] += 1

        for location in reversed(range(1, 7)):
            if counts[location] >= 3:
                return location * 3
        return 0

    @staticmethod
    def four_of_a_kind(hand):
        counts = dict.fromkeys(range(1, 7), 0)
        for die in hand.dice:
            counts[die] += 1

        for location in reversed(range(1, 7)):
            if counts[location] >= 4:
                return location * 4
        return 0

    @staticmethod
    def small_straight(hand):
        hand.dice.sort()
        if hand.dice == [1, 2, 3, 4, 5]:
            return 15
        else:
            return 0

    @staticmethod
    def large_straight(hand):
        hand.dice.sort()
        if hand.dice == [2, 3, 4, 5, 6]:
            return 20
        else:
            return 0

    @staticmethod
    def full_house(hand):
        counts = dict.fromkeys(range(1, 7), 0)
        for die in hand.dice:
            counts[die] += 1

        if 2 in counts.values() and 3 in counts.values():
            return sum(hand.dice)
        return 0


def single_number(hand, number):
    sum = 0
    for die in hand.dice:
        if die == number:
            sum += die
    return sum
