#!/bin/python3
# Problem description: https://www.hackerrank.com/challenges/balanced_brackets/
# GitHub: https://github.com/kwasnydam

import os

CORRECT_BRACKETS_PAIRS = set(['()','[]','{}'])
OPENING_BRACKETS = set(['(','[','{'])

def isBalanced(s):
    brackets_stack = list()
    for bracket in s:
        if bracket in OPENING_BRACKETS:
            brackets_stack.append(bracket)
        else:
            try:
                last_bracket = brackets_stack.pop()
                brackets_pair = ''.join([last_bracket, bracket])
                if brackets_pair not in CORRECT_BRACKETS_PAIRS:
                    return 'NO'
            except IndexError:
                return 'NO'
    if brackets_stack:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
