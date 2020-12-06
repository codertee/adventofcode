# Advent of Code challenge solutions
## Install
You can do `python setup.py install` to install adventofcode binary.
If you want to run the code without installing, add repo root to `PYTHONPATH`.
## Usage
`adventofcode` or `python -m adventofcode` runs all solutions for the current year.
You need to log in to [adventofcode.com](https://adventofcode.com), inspect HTTP requests, 
check the cookies and add the session id to `AOC_SESSION_ID` environment variable. 
Alternatively, you can set the session id as `python -m adventofcode -s <session_id>`.
### Examples
- `adventofcode 6` solves day 6 of current challenges.
- `adventofcode -y 2019` solves all 2019 challenges (currently not implemented).
- `adventofcode -p 2` solves part two of all current challenges.