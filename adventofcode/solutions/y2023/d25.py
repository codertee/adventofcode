import os
import re
from collections import defaultdict, deque
from functools import partial
from multiprocessing import Pool

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    graph = defaultdict(set)
    for line in input_str.splitlines():
        name, *links = re.findall(r"\w+", line)
        graph[name].update(links)
        for link in links:
            graph[link].add(name)
    return graph


def check_path(graph: dict[str, set], start: str, paths: list, check: str):
    q = deque([(start, [start])])
    seen = set()
    while q:
        node, path = q.popleft()
        for nxt in graph[node]:
            if nxt == check:
                paths.update(path)
                return 1
            if nxt in seen or nxt in paths:
                continue
            seen.add(nxt)
            q.append((nxt, path + [nxt]))
    return 0


def check_connection(graph: dict[str, set], first: str, check: str):
    nodes = set(graph[first])
    connections = int(check in nodes)
    nodes.discard(check)
    paths = {first}
    for start in nodes:
        connections += check_path(graph, start, paths, check)
    return connections >= 4


@aoc_timer(1, 25, 2023)
def solve_first(graph):
    first, *nodes = graph.keys()
    connected = 1
    with Pool(os.cpu_count() // 2) as p:
        connected += sum(p.map(partial(check_connection, graph, first), nodes))
    return connected * (len(graph) - connected)


if __name__ == "__main__":
    graph = parse_input(get_input(25, year=2023))
    solve_first(graph)
