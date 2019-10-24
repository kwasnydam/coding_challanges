#!/bin/python3
# Implementing the array inversion count algorithm with merge sort. From
# https://www.coursera.org/learn/algorithms-divide-conquer/lecture/GFmmJ/o-n-log-n-algorithm-for-counting-inversions-i
# GitHub: https://github.com/kwasnydam

def count_inversions(array):
    if len(array) <= 1:
        return 0, array
    middle_point = len(array)//2
    inversions_a, sorted_a = count_inversions(array[:middle_point])
    inversions_b, sorted_b = count_inversions(array[middle_point:])
    split_inversions, sorted_array = count_split_inversions(sorted_a, sorted_b)
    return inversions_a + inversions_b + split_inversions, sorted_array

def count_split_inversions(array_a, array_b):
    index_a = index_b = index_c = 0
    array_c = []
    split_inversions_count = 0
    while index_c < (len(array_a)+len(array_b)):
        if index_a < len(array_a) and index_b < len(array_b):
            if array_a[index_a] <= array_b[index_b]:
                array_c.append(array_a[index_a])
                index_a += 1
            else:
                array_c.append(array_b[index_b])
                split_inversions_count += len(array_a) - index_a
                index_b += 1
        else:
            if index_a >= len(array_a):
                array_c.append(array_b[index_b])
                index_b += 1
            else:
                array_c.append(array_a[index_a])
                index_a += 1
        index_c += 1

    return split_inversions_count, array_c
