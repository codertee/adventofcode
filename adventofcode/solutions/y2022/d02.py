from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    strategy = map(str.split, input_str.splitlines())
    strategy = map(tuple, strategy)
    return list(strategy)


ROCK, PAPER, SCISSORS = 1, 2, 3
LOSE, DRAW, WIN = 0, 3, 6


@aoc_timer(1, 2, 2022)
def solve_first(strategy):
    decrypt = {
        'A': ROCK, 'B': PAPER, 'C': SCISSORS,
        'X': ROCK, 'Y': PAPER, 'Z': SCISSORS
    }
    wins = {(ROCK, SCISSORS), (PAPER, ROCK), (SCISSORS, PAPER)}
    score = 0
    for elf, player in strategy:
        elf, player = decrypt[elf], decrypt[player]
        score += player
        if (player, elf) in wins:
            score += WIN
        elif player == elf:
            score += DRAW
    return score


@aoc_timer(2, 2, 2022)
def solve_second(strategy):
    decrypt = {
        'A': ROCK, 'B': PAPER, 'C': SCISSORS,
        'X': LOSE, 'Y': DRAW, 'Z': WIN
    }
    choices = {
        (PAPER, LOSE): ROCK, (ROCK, DRAW): ROCK, (SCISSORS, WIN): ROCK,
        (SCISSORS, LOSE): PAPER, (PAPER, DRAW): PAPER, (ROCK, WIN): PAPER,
        (ROCK, LOSE): SCISSORS, (SCISSORS, DRAW): SCISSORS, (PAPER, WIN): SCISSORS,
    }
    score = 0
    for elf, player in strategy:
        elf, player = decrypt[elf], decrypt[player]
        score += player
        score += choices[(elf, player)]
    return score


if __name__ == '__main__':
    strategy = parse_input(get_input(2, year=2022))
    solve_first(strategy)
    solve_second(strategy)
