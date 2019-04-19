#!/usr/bin/env python3

import re
from subprocess import getoutput, getstatusoutput

prg = './make_chocolate.py'

def test_usage():
    rv, out = getstatusoutput('{}'.format(prg))
    assert rv > 0
    assert re.match('usage', out, re.IGNORECASE)

def make_chocolate(small, big, goal):
    big_use = goal//5
    if big >= big_use:
      small_use = goal - 5 * big_use
    else:
      small_use = goal - 5 * big
    if small >= small_use:
      return small_use
    else:
      return 'The goal chocolate cannot be done'

def test_runs():
    tests = [
        (4, 1, 9),
        (4, 1, 10),
        (6, 2, 10),
        (1, 2, 7),
        (4, 1, 4),
        (1000, 1000000, 5000006),
    ]

    for small, big, goal in tests:
        expected = make_chocolate(small, big, goal)
        try:
            out = int(getoutput('{} {} {} {}'.format(prg, small, big, goal)))
        except:
            out = getoutput('{} {} {} {}'.format(prg, small, big, goal))
        assert expected == out
