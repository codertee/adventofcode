from adventofcode.inputs import get_input


def parse_input(input_str):
    return list(map(int, input_str.split()))


def solve_first(expenses):
    for i in range(len(expenses)):
        for j in range(i, len(expenses)):
            x, y = expenses[i], expenses[j]
            if x + y == 2020:
                print('2020.1 part one:', x*y)
                break


def solve_second(expenses):
    for i in range(len(expenses)):
        for j in range(i, len(expenses)):
            for k in range(j, len(expenses)):
                x, y, z = expenses[i], expenses[j], expenses[k]
                if x + y + z == 2020:
                    print('2020.1 part two:', x*y*z)
                    break


if __name__ == '__main__':
    expenses = parse_input(get_input(1, year=2020))
    solve_first(expenses)
    solve_second(expenses)
