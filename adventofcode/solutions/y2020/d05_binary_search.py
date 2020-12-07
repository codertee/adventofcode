from math import ceil

from adventofcode.inputs import get_input


def parse_input(input_str):
    return input_str.splitlines()


def binary_search(seq, low, high, half, instr_low):
    instr = seq.pop()
    half = ceil(half / 2)
    if instr == instr_low:
        high = high - half
    else:
        low = low + half
    if not seq:
        return low if instr == instr_low else high
    return binary_search(seq, low, high, half, instr_low)


def position(bpass):
    rows, columns = bpass[:7], bpass[7:]
    row = binary_search(list(reversed(rows)), 0, 127, 127, 'F')
    col = binary_search(list(reversed(columns)), 0, 7, 7, 'L')
    return row, col


def compile_list(boarding_passes):
    boarding_id_lst = []
    for bpass in boarding_passes:
        row, col = position(bpass)
        boarding_id_lst.append(row * 8 + col)
    return boarding_id_lst


def solve_first(boarding_passes):
    print('2020.5 part one:', max(compile_list(boarding_passes)))


def solve_second(boarding_passes):
    sorted_bid_lst = sorted(compile_list(boarding_passes))
    for i in range(1, len(sorted_bid_lst)):
        boarding_id = sorted_bid_lst[i]
        if sorted_bid_lst[i - 1] + 2 == boarding_id:
            print('2020.5 part two:', boarding_id - 1)
            break


if __name__ == '__main__':
    boarding_passes = parse_input(get_input(5, year=2020))
    solve_first(boarding_passes)
    solve_second(boarding_passes)
