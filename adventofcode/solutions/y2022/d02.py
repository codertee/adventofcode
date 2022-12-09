from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return input_str.splitlines()


ROCK, PAPER, SCISSORS = 1, 2, 3
LOSE, DRAW, WIN = 0, 3, 6


@aoc_timer(1, 2, 2022)
def solve_first(turns):
    lookup = {
        'A X': ROCK + DRAW, 'A Y': PAPER + WIN, 'A Z': SCISSORS + LOSE,
        'B X': ROCK + LOSE, 'B Y': PAPER + DRAW, 'B Z': SCISSORS + WIN,
        'C X': ROCK + WIN, 'C Y': PAPER + LOSE, 'C Z': SCISSORS + DRAW
    }
    return sum(map(lookup.get, turns))


@aoc_timer(2, 2, 2022)
def solve_second(turns):
    lookup = {
        'A X': LOSE + SCISSORS, 'A Y': DRAW + ROCK, 'A Z': WIN + PAPER,
        'B X': LOSE + ROCK, 'B Y': DRAW + PAPER, 'B Z': WIN + SCISSORS,
        'C X': LOSE + PAPER, 'C Y': DRAW + SCISSORS, 'C Z': WIN + ROCK
    }
    return sum(map(lookup.get, turns))


if __name__ == '__main__':
    turns = parse_input(get_input(2, year=2022))
    solve_first(turns)
    solve_second(turns)
