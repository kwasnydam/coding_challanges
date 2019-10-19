#!/bin/python3
# Problem description: https://www.hackerrank.com/challenges/minimum-time-required/
# GitHub: https://github.com/kwasnydam

import math
import os

def minTime(machines, goal):
    """
    kind of a bisection algorithm to find roots(https://en.wikipedia.org/wiki/Bisection_method).
    The variable we are optimizing for is number of days. Every iterations we cut the
    searching space by half
    """
    lower_bound = 1
    upper_bound = get_worst_case_scenario(machines, goal)

    while lower_bound <= upper_bound:
        middle_point = lower_bound + (upper_bound-lower_bound)//2
        if items_produced_in_n_days(middle_point, machines) >= goal:
            upper_bound = middle_point
        else:
            lower_bound = middle_point
        if items_produced_in_n_days(middle_point, machines) < goal and items_produced_in_n_days(middle_point+1, machines) >= goal:
            return middle_point + 1

    return lower_bound

def get_worst_case_scenario(machines, goal):
    """
    In the worst case scenario, if all machines are as slow as the slowest, it would take
    (num_of_items(goal)*days_per_item_per_machine(max(machnies))/num_of_machines(len(machines))
    """
    return int((max(machines)*goal)/len(machines))

def items_produced_in_n_days(n, machines):
    """
    in n days, a machine finishes n/days_per_item items. To get all items produced
    in n days, we need to sum over all machines
    """
    return sum([n//machine for machine in machines])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
