#!/bin/env python3

# Link: https://www.hackerrank.com/challenges/string-validators

def compute(s):
    has_alnum = any([c.isalnum() for c in s])
    has_alpha = any([c.isalpha() for c in s])
    has_digit = any([c.isdigit() for c in s])
    has_lower = any([c.islower() for c in s])
    has_upper = any([c.isupper() for c in s])

    return [has_alnum, has_alpha, has_digit, has_lower, has_upper]


if __name__ == '__main__':
    s = input()
    print("\n".join([str(b) for b in compute(s)]))
