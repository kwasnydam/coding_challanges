#!/bin/python3
# Problem description: https://www.hackerrank.com/challenges/triple_sum/
# GitHub: https://github.com/kwasnydam

import os
from bisect import bisect_right

def transform_to_sorted_unique_array(array):
    unique_set = set(array)
    sorted_unique_array = sorted(list(unique_set))
    return sorted_unique_array

def find_le_index(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i
    else:
        return None

def triplets(a, b, c):
    a_transformed = transform_to_sorted_unique_array(a)
    b_transformed = transform_to_sorted_unique_array(b)
    c_transformed = transform_to_sorted_unique_array(c)
    triplets_count = 0
    for element in b_transformed:
        a_less_equal = find_le_index(a_transformed, element)
        c_less_equal = find_le_index(c_transformed, element)

        if a_less_equal is not None and c_less_equal is not None:
            triplets_count += a_less_equal*c_less_equal
    return triplets_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
