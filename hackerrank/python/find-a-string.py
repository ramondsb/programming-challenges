#!/usr/bin/env python3

# Link: https://www.hackerrank.com/challenges/find-a-string

def count_substring(original, substring):
    counter = 0
    substring_size = len(substring)
    size_range = len(original) - substring_size + 1

    for i in range(size_range):
        partial = original[i: i + substring_size]
        if partial == substring:
            counter += 1

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
