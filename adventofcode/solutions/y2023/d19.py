import re
from math import prod
from operator import gt, lt

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_rule(rule: str):
    m = re.match(r"(\w)(<|>)(\d+):(\w+)", rule)
    if not m:
        return rule
    cat, op, amt, target = m.groups()
    return "xmas".index(cat), op, int(amt), target


def parse_input(input_str):
    workflows, parts_str = input_str.split("\n\n")
    flows = {}
    for line in workflows.splitlines():
        label, rules_str = re.match(r"(\w+)\{(.*)\}", line).groups()
        flows[label] = list(map(parse_rule, rules_str.split(",")))
    parts = []
    for line in parts_str.splitlines():
        parts.append(list(map(int, re.findall(r"\d+", line))))
    return flows, parts


def acceptable(flows, part, label):
    if label == "A":
        return part
    if label == "R":
        return []
    *rules, last = flows[label]
    for idx, op, amt, target in rules:
        if {">": gt, "<": lt}[op](part[idx], amt):
            return acceptable(flows, part, target)
    return acceptable(flows, part, last)


@aoc_timer(1, 19, 2023)
def solve_first(flows, parts):
    return sum(sum(acceptable(flows, p, "in")) for p in parts)


def split_ranges(flows, ranges, label):
    if label == "A":
        yield prod(end - start + 1 for start, end in ranges); return
    elif label == "R":
        yield 0; return
    *rules, last = flows[label]
    for idx, op, amt, target in rules:
        start, end = ranges[idx]
        if op == "<":
            nxt = start < amt and (start, amt - 1)
            ranges[idx] = (max(start, amt), end)
        else:
            nxt = end > amt and (amt + 1, end)
            ranges[idx] = (start, min(end, amt))
        if nxt:
            nxt_ranges = ranges[:idx] + [nxt] + ranges[idx + 1:]
            yield from split_ranges(flows, nxt_ranges, target)
    yield from split_ranges(flows, ranges, last)


@aoc_timer(2, 19, 2023)
def solve_second(flows, _):
    ranges = [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]
    return sum(split_ranges(flows, ranges, "in"))


if __name__ == "__main__":
    flows, parts = parse_input(get_input(19, year=2023))
    solve_first(flows, parts)
    solve_second(flows, parts)
