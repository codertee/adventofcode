from adventofcode.inputs import get_input


def parse_input(input_str):
    return input_str.splitlines()


def solve_first(policies):
    valid = 0
    for line in policies:
        policy, password = line.split(": ")
        counts, letter = policy.split()
        count_low, count_high = counts.split('-')
        if int(count_low) <= password.count(letter) <= int(count_high):
            valid += 1
    print('2020.2 part one:', valid)


def solve_second(policies):
    valid = 0
    for line in policies:
        policy, password = line.split(": ")
        positions, letter = policy.split()
        pos1, pos2 = positions.split('-')
        l1 = password[int(pos1) - 1]
        l2 = password[int(pos2) - 1]
        if [l1, l2].count(letter) == 1:
            valid += 1
    print('2020.2 part two:', valid)


if __name__ == '__main__':
    policies = parse_input(get_input(2, year=2020))
    solve_first(policies)
    solve_second(policies)





