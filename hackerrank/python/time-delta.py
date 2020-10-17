#!/usr/bin/env python3

# Link: https://www.hackerrank.com/challenges/python-time-delta


import os
import random
import re
import sys
from datetime import datetime


def time_delta(t1, t2):
    def str_to_datetime(t):
        return datetime.strptime(t, "%a %d %b %Y %H:%M:%S %z")

    datetime_t1 = str_to_datetime(t1)
    datetime_t2 = str_to_datetime(t2)

    return int(abs((datetime_t1 - datetime_t2).total_seconds()))


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(str(delta) + '\n')
