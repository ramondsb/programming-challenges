#!/bin/env python3

# Link: https://www.hackerrank.com/challenges/swap-case


def swap_case(s):
    return "".join(map(lambda c: c.lower() if c.isupper() else c.upper(), s))


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

