"""
Given an array of numbers, determine subset which adds up exactly to the
target  sum.

1. Assume all numbers are positive integers

2. If no subset can be found return None

"""

import time


def recursive_howSum(t, arr, series=None):
    """
    Recursive implementation. Time complexity O(t^n * t) where n is len(arr).

    """
    if t == 0: return []
    if t < min(arr): return None

    for v in arr:
        result = recursive_howSum(t-v, arr)
        if result != None:
            return  result + [v]
    
    return None


if __name__ == '__main__':
    assert recursive_howSum(7, [5, 3, 7]) == [7]
    assert set(recursive_howSum(7, [4, 3])) == set([3, 4])
    assert recursive_howSum(7, [5, 3]) is None
    print("Recursive OK!")