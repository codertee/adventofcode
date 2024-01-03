import re

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_group(g: str):
    return [
        [int(d) for d in re.findall(r"\d+", l)]
        for l in g.splitlines()[1:]
    ]


def parse_input(input_str: str):
    seeds, *groups = input_str.split("\n\n")
    seeds = list(map(int, re.findall(r"\d+", seeds)))
    return seeds, list(map(parse_group, groups))


def check(mapping, item):
    for dst, src, delta in mapping:
        if src <= item < src + delta:
            return item + dst - src
    return item


@aoc_timer(1, 5, 2023)
def solve_first(seeds, mappings):
    lowest = 1e100
    for seed in seeds:
        for m in mappings:
            seed = check(m, seed)
        lowest = min(lowest, seed)
    return lowest


def split(mapping, ranges):
    nxt_ranges = []
    while ranges:
        start, end = ranges.pop()
        for dst, src, delta in mapping:
            left, right = max(start, src), min(end, src + delta)
            if left >= right:
                continue
            nxt_ranges.append((left + dst - src, right + dst - src))
            if start < left:
                ranges.append((start, left))
            if right < end:
                ranges.append((right, end))
            break
        else:
            nxt_ranges.append((start, end))
    return nxt_ranges


@aoc_timer(2, 5, 2023)
def solve_second(seeds, mappings):
    ranges = [(start, start + delta) for start, delta in zip(seeds[::2], seeds[1::2])]
    for m in mappings:
        ranges = split(m, ranges)
    start, _ = min(ranges)
    return start


if __name__ == "__main__":
    ranges, mapping = parse_input(get_input(5, year=2023))
    solve_first(ranges, mapping)
    solve_second(ranges, mapping)
