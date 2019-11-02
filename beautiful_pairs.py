#!/bin/python3

from collections import Counter

def beautiful_pairs(a, b):
    '''
    Beautiful Pair function should return an integer that represents
    the maximum number of pairwise disjoint beautiful pairs that can be formed.

    If a[i] is equal to b[i], it is called beautiful pairs.
    A set containing beautiful pairs is called a beautiful set.

    The task is to change exactly 1 element in "b" so that the size of the
    pairwise disjoint beautiful set is maximum.

    Example
    a = [1 2 3 4 5]
    b = [2 3 4 5 6]

    if we change b[4] to 1, then maximum beautiful pairs will be 5, hence result is 5
    '''

    # length of first array
    n = len(a)

    # Here counter is used to keep track of no of occurences
    ca, cb = Counter(a), Counter(b)
    common = sum(min(ca[k], cb[k]) for k in ca.keys())

    return common-1 if common==n else common+1


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = beautiful_pairs(a, b)
    print(result)