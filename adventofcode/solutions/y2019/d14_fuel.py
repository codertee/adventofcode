from collections import defaultdict
from math import ceil

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_chem(s):
    n, chem = s.split()
    return chem, int(n)


def parse_equation(s):
    reactants, prod = s.split(" => ")
    reactants = dict(map(parse_chem, reactants.split(", ")))
    chem, n = parse_chem(prod)
    return chem, (n, reactants)


def parse_input(input_str):
    return dict(map(parse_equation, input_str.splitlines()))


def ore_needed(reactions, chem, n_input, leftovers=defaultdict(int)):
    n_current, reactants = reactions[chem]
    # n_current chemicals produces n_input chemicals, normalize it
    output_factor = int(ceil(n_input / n_current))
    leftovers[chem] += output_factor * n_current - n_input
    if n_ore := reactants.get("ORE"):
        yield output_factor * n_ore
        return
    # components of input chemical
    for comp, n_comp in reactants.items():
        component_factor = n_comp * output_factor
        leftovers_used = min(leftovers[comp], component_factor)
        component_factor -= leftovers_used
        leftovers[comp] -= leftovers_used
        yield from ore_needed(reactions, comp, component_factor)


def get_fuel(reactions, n_fuel):
    # [0] is fuel amount, but puzzle input is always 1
    reactants = reactions["FUEL"][1]
    total_ore = 0
    for chem, n_current in reactants.items():
        total_ore += sum(ore_needed(reactions, chem, n_fuel * n_current))
    return total_ore


@aoc_timer(1, 14, 2019)
def solve_first(reactor_equations):
    return get_fuel(reactor_equations, 1)


@aoc_timer(2, 14, 2019)
def solve_second(reactor_equations):
    trillion = 1000000000000
    high, low = trillion, 0
    while high - low > 1:
        fuel = (high + low) // 2
        if get_fuel(reactor_equations, fuel) > trillion:
            high = fuel
        else:
            low = fuel
    return low


if __name__ == "__main__":
    reactor_equations = parse_input(get_input(14, year=2019))
    solve_first(reactor_equations)
    solve_second(reactor_equations)
