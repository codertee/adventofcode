import sys

from adventofcode import parse_args
from adventofcode.inputs import get_input
from adventofcode.solutions import SOLVED


def execute():
    args = parse_args()
    year = args.year
    day = args.day
    solutions = SOLVED.get(year)
    if not solutions:
        sys.exit(f'no solutions implemented for {year} challenges.')
    if day == 0:
        challenge_solvers = solutions
    else:
        solver = solutions.get(day)
        if not solver:
            sys.exit(f'no solution implemented for {day}. December {year}.')
        challenge_solvers = {day: solver}
    challenges = []
    print('collecting challenge inputs')
    for d, module in challenge_solvers.items():
        try:
            input_str = get_input(d, year=year)
        except Exception as e:
            sys.exit(f'exception when collecting December {d}. {year} challenge input: {e}\n'
                     f'check network or session cookie')
        challenge_input = module.parse_input(input_str)
        if args.part == 0:
            challenges.append((challenge_input, module.solve_first))
            challenges.append((challenge_input, module.solve_second))
        elif args.part == 1:
            challenges.append((challenge_input, module.solve_first))
        else:
            challenges.append((challenge_input, module.solve_second))
    for challenge_input, solve in challenges:
        solve(challenge_input)
