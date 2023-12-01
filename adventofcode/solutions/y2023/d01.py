import re
import string

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


SPELLED = "one, two, three, four, five, six, seven, eight, nine".split(", ")
TRANSFORM = {d: d for d in string.digits}
TRANSFORM.update(dict(zip(SPELLED, string.digits[1:])))


def parse_input(input_str):
    return input_str


def compile_numbers(doc: str, regex: str):
    for l in doc.splitlines():
        digits = re.findall(regex, l)
        first, last = digits[0], digits[-1]
        yield int(TRANSFORM[first] + TRANSFORM[last])


@aoc_timer(1, 1, 2023)
def solve_first(doc):
    return sum(compile_numbers(doc, r"\d"))


@aoc_timer(2, 1, 2023)
def solve_second(doc):
    digits_regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    return sum(compile_numbers(doc, digits_regex))


if __name__ == "__main__":
    doc = parse_input(get_input(1, year=2023))
    solve_first(doc)
    solve_second(doc)
