from adventofcode.inputs import get_input


def parse_input(input_str):
    return input_str.split('\n\n')


def solve_first(answers_lst):
    counts = 0
    for group in answers_lst:
        group_count = set()
        for person_answers in group.split():
            group_count.update(person_answers)
        counts += len(group_count)
    print('2020.6 part one:', counts)


def solve_second(answers_lst):
    counts = 0
    for group in answers_lst:
        group_lst = group.split()
        group_count = set(group_lst[0])
        for person_answers in group_lst[1:]:
            group_count = group_count.intersection(person_answers)
        counts += len(group_count)
    print('2020.6 part two:', counts)


if __name__ == '__main__':
    answers = parse_input(get_input(6, year=2020))
    solve_first(answers)
    solve_second(answers)