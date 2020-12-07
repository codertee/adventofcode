import time


def aoc_timer(part: int, day: int, year: int = 2020):
    part = {1: 'one', 2: 'two'}[part]
    identifier_str = f'{year}.{day} part {part}'
    def decorator(func):
        def wrapper(parsed_input):
            try:
                start = time.perf_counter()
                result = func(parsed_input)
                delta = (time.perf_counter() - start) * 1000
                print(f'{identifier_str}: {result} ({delta:.4f} ms)')
            except Exception as e:
                print(f'exception when solving {identifier_str} challenge: {e}')
            else:
                return result
        return wrapper
    return decorator