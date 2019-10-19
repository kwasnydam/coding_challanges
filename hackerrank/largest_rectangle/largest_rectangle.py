#!/bin/python3
# Problem description: https://www.hackerrank.com/challenges/largest-rectangle/
# GitHub: https://github.com/kwasnydam

import os

def largestRectangle(h):
    stack = [0]
    max_area = 0
    index = 1
    while index < len(h):

        if (stack and h[index] >= h[stack[-1]]) or not stack:
            stack.append(index)
            index += 1
        else:
            if len(stack) > 1:
                current_area = h[stack.pop()] * (index - 1 - stack[-1])
            else:
                current_area = h[stack.pop()]*index
            if current_area > max_area:
                max_area = current_area

    index = len(h) - 1
    while len(stack) > 1:
        current_area = h[stack.pop()] * (index - stack[-1])
        if current_area > max_area:
            max_area = current_area
    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
