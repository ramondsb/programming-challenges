#!/usr/bin/env python3

# Link: https://www.hackerrank.com/challenges/no-idea/problem

def happiness_score(n, a, b):
    join = {}
    for elem in a:
        join[elem] = 1

    for elem in b:
        join[elem] = -1

    return sum([join.get(elem, 0) for elem in n ])


if __name__ == "__main__":
    _ = list(input().split())
    n = list(input().split())
    a = list(input().split())
    b = list(input().split())

    print(happiness_score(n, a, b))
