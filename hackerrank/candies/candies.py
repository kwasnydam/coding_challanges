#!/bin/python3
# Problem description: https://www.hackerrank.com/challenges/candies/
# GitHub: https://github.com/kwasnydam

import os

def candies(n, arr):
    result = [0 for _ in range(n)]
    start = 1 if arr[0] <= arr[1] else 2
    result[0] = start
    decresing_subsequence_start_index = None
    for index in range(1, len(arr)):
        if current_rate_higher_then_preceeding(arr, index):
            result = give_current_child_one_more_candy_then_previous_child(result, index)
            decresing_subsequence_start_index = None
        else:
            result[index] = 1
            if decresing_subsequence_start_index is None:
                decresing_subsequence_start_index = index - 1
            else:
                result = increase_values_in_current_descending_subsequence_if_necessary(
                    result, arr, index, decresing_subsequence_start_index
                )
    return sum(result)

def current_rate_higher_then_preceeding(arr, index):
    return arr[index] > arr[index-1]

def increase_values_in_current_descending_subsequence_if_necessary(result, arr, index, decresing_subsequence_start_index):
    for decresing_subsequence_index in range(index, decresing_subsequence_start_index, -1):
        if result[decresing_subsequence_index] >= result[decresing_subsequence_index-1]:
            if arr[decresing_subsequence_index-1] > arr[decresing_subsequence_index]:
                result[decresing_subsequence_index-1] += 1
    return result

def give_current_child_one_more_candy_then_previous_child(result, index):
    result[index] = result[index - 1] + 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
