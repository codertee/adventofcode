import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('day', default=0, type=int, nargs='?',
                        help='challenge calendar day, 0 solves all')
    parser.add_argument('-p', '--part', dest='part', default=0, type=int, choices=range(3),
                        help='solve task part 1 or 2, 0 solves both')
    parser.add_argument('-y', '--year', dest='year', default=2020, type=int, choices=range(2015, 2021),
                        help='solve tasks from this year')
    parser.add_argument('-c', '--cache', dest='cache_dir', 
                        help='directory where to store challenge input strings')
    parser.add_argument('-s', '--session', dest='session',
                        help='adventofcode.com login session cookie')
    return parser.parse_args()
