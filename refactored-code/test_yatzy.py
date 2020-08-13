from yatzy import Hand, Scoring, Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance():
    assert 5 == Scoring.chance(Hand(1, 1, 1, 1, 1))
    assert 15 == Scoring.chance(Hand(2, 3, 4, 5, 1))
    assert 16 == Scoring.chance(Hand(3, 3, 4, 5, 1))
    assert 30 == Scoring.chance(Hand(6, 6, 6, 6, 6))


def test_yatzy():
    assert 50 == Scoring.yatzy(Hand(4, 4, 4, 4, 4))
    assert 50 == Scoring.yatzy(Hand(6, 6, 6, 6, 6))
    assert 0 == Scoring.yatzy(Hand(6, 6, 6, 6, 3))
    assert 0 == Scoring.yatzy(Hand(1, 2, 3, 4, 5))


def test_ones():
    assert 1 == Scoring.ones(Hand(1, 2, 3, 4, 5))
    assert 2 == Scoring.ones(Hand(1, 2, 1, 4, 5))
    assert 0 == Scoring.ones(Hand(6, 2, 2, 4, 5))
    assert 4 == Scoring.ones(Hand(1, 2, 1, 1, 1))


def test_twos():
    assert 4 == Scoring.twos(Hand(1, 2, 3, 2, 6))
    assert 10 == Scoring.twos(Hand(2, 2, 2, 2, 2))
    assert 0 == Scoring.twos(Hand(1, 3, 4, 5, 6))


def test_threes():
    assert 6 == Scoring.threes(Hand(1, 2, 3, 2, 3))
    assert 12 == Scoring.threes(Hand(2, 3, 3, 3, 3))
    assert 0 == Scoring.threes(Hand(1, 2, 4, 5, 6))


def test_fours():
    assert 12 == Scoring.fours(Hand(4, 4, 4, 5, 5))
    assert 8 == Scoring.fours(Hand(4, 4, 5, 5, 5))
    assert 4 == Scoring.fours(Hand(4, 5, 5, 5, 5))
    assert 0 == Scoring.fours(Hand(1, 2, 3, 5, 6))


def test_fives():
    assert 10 == Scoring.fives(Hand(4, 4, 4, 5, 5))
    assert 15 == Scoring.fives(Hand(4, 4, 5, 5, 5))
    assert 20 == Scoring.fives(Hand(4, 5, 5, 5, 5))
    assert 0 == Scoring.fives(Hand(1, 2, 3, 4, 6))


def test_sixes():
    assert 0 == Scoring.sixes(Hand(4, 4, 4, 5, 5))
    assert 6 == Scoring.sixes(Hand(4, 4, 6, 5, 5))
    assert 18 == Scoring.sixes(Hand(6, 5, 6, 6, 5))


def test_one_pair():
    assert 6 == Scoring.pair(Hand(3, 4, 3, 5, 6))
    assert 10 == Scoring.pair(Hand(5, 3, 3, 3, 5))
    assert 12 == Scoring.pair(Hand(5, 3, 6, 6, 5))
    assert 0 == Scoring.pair(Hand(1, 2, 3, 4, 5))


def test_two_pair():
    assert 16 == Scoring.two_pair(Hand(3, 3, 5, 4, 5))
    assert 18 == Scoring.two_pair(Hand(3, 3, 6, 6, 6))
    assert 0 == Scoring.two_pair(Hand(3, 3, 6, 5, 4))


def test_three_of_a_kind():
    assert 9 == Scoring.three_of_a_kind(Hand(3, 3, 3, 4, 5))
    assert 15 == Scoring.three_of_a_kind(Hand(5, 3, 5, 4, 5))
    assert 9 == Scoring.three_of_a_kind(Hand(3, 3, 3, 3, 5))
    assert 0 == Scoring.three_of_a_kind(Hand(3, 3, 2, 2, 1))


def test_four_of_a_kind():
    assert 12 == Scoring.four_of_a_kind(Hand(3, 3, 3, 3, 5))
    assert 20 == Scoring.four_of_a_kind(Hand(5, 5, 5, 4, 5))
    assert 12 == Scoring.four_of_a_kind(Hand(3, 3, 3, 3, 3))
    assert 0 == Scoring.four_of_a_kind(Hand(3, 3, 3, 2, 1))


def test_small_straight():
    assert 15 == Scoring.small_straight(Hand(1, 2, 3, 4, 5))
    assert 15 == Scoring.small_straight(Hand(2, 3, 4, 5, 1))
    assert 0 == Scoring.small_straight(Hand(1, 2, 2, 4, 5))


def test_large_straight():
    assert 20 == Scoring.large_straight(Hand(6, 2, 3, 4, 5))
    assert 20 == Scoring.large_straight(Hand(2, 3, 4, 5, 6))
    assert 0 == Scoring.large_straight(Hand(1, 2, 2, 4, 5))


def test_full_house():
    assert 18 == Scoring.full_house(Hand(6, 2, 2, 2, 6))
    assert 0 == Scoring.full_house(Hand(2, 3, 4, 5, 6))

