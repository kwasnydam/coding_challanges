#!/bin/python3
# Problem description: https://www.hackerrank.com/challenges/pairs/
# GitHub: https://github.com/kwasnydam

import os

def pairs(k, arr):
    present_numbers = set(arr)
    pairs_count = 0
    for value in arr:
        complement = value - k
        if complement in present_numbers:
            pairs_count += 1
    return pairs_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
