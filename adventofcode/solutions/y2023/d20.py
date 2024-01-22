import math
from collections import deque
from copy import deepcopy
from dataclasses import make_dataclass
from itertools import count

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


M = make_dataclass("Module", ["type", "label", "dests", "state"])


def parse_line(line: str):
    label, dests = line.split(" -> ")
    dests = dests.split(", ")
    if label == "broadcaster":
        return M(label, label, dests, False)
    else:
        t, l = label[0], label[1:]
        return M(t, l, dests, False if t == "%" else {})


def parse_input(input_str):
    modules = map(parse_line, input_str.splitlines())
    modules = {m.label: m for m in modules}
    for label, module in modules.items():
        for dst in module.dests:
            if dst in modules and modules[dst].type == "&":
                modules[dst].state[label] = False
    return modules


def send(module, state):
    return [(module.label, dst, state) for dst in module.dests]


def propagate(module: M, src: str, state: bool):
    if module.type == "%":
        if state:
            return []
        nxt_state = module.state = not module.state
    else:
        module.state[src] = state
        nxt_state = not all(module.state.values())
    return send(module, nxt_state)


@aoc_timer(1, 20, 2023)
def solve_first(modules):
    modules = deepcopy(modules)
    lows = highs = 0
    for _ in range(1000):
        lows += 1
        q = deque(send(modules["broadcaster"], False))
        while q:
            src, dst, state = q.popleft()
            lows += not state
            highs += state
            if dst not in modules:
                continue
            q += propagate(modules[dst], src, state)
    return lows * highs


@aoc_timer(2, 20, 2023)
def solve_second(modules: dict[str, M]):
    cycles = {}
    cycler = next(m.label for m in modules.values() if "rx" in m.dests)
    seen = {name: False for name, m in modules.items() if cycler in m.dests}
    for c in count(1):
        q = deque(send(modules["broadcaster"], False))
        while q:
            src, dst, state = q.popleft()
            if dst not in modules:
                continue
            if dst == cycler and state:
                seen[src] = True
                if src not in cycles:
                    cycles[src] = c
                if all(seen.values()):
                    return math.lcm(*cycles.values())
            q += propagate(modules[dst], src, state)


if __name__ == "__main__":
    a = parse_input(get_input(20, year=2023))
    solve_first(a)
    solve_second(a)
