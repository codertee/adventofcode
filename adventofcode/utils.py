import logging
import time


def aoc_timer(part=0, day=0, year=0):
    part = {1: 'one', 2: 'two'}.get(part)
    prepend = ''
    if year:
        prepend += '%s.' % year
    if day:
        prepend += '%s ' % day
    if part:
        prepend += 'part %s: ' % part
    def decorator(func):
        def wrapper(*a, **kw):
            try:
                start = time.perf_counter()
                result = func(*a, **kw)
                delta = (time.perf_counter() - start) * 1000
                if not prepend:
                    print(f'finished {func.__name__} in {delta:.4f} ms')
                else:
                    print(f'{prepend}{result} ({delta:.4f} ms)')
            except Exception as e:
                logging.exception(f'exception when solving {prepend}: {e}')
            else:
                return result
        return wrapper
    return decorator
