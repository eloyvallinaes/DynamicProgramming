"""
Determine whether the shortest combination of numbers in arr that can be
added to produce a target value.

1. Array values may be used as many times as necessary.

2. All input values are positive integers.

3. Ties for shortest combination may return either.


"""

import math
from canSum import timeit

def recursive_bestSum(t, arr):
    """
    Recursive implementation. Time complexity: O(m^t * t)
        Recursive calls: O(m^t) where len(arr) = m
        List extension: O(k) where len(list) = k

    """
    # end cases
    if t == 0: return []
    if t < min(arr): return None

    best = None
    for v in arr:
        result = recursive_bestSum(t-v, arr)
        if result is not None:
            if  best is None or len(result) <= len(best):
                best = [v] + result  # list extension
        
    return best


if __name__ == "__main__":
    assert set(recursive_bestSum(7, [1, 2, 5])) == set([2, 5])
    assert recursive_bestSum(7, [3, 5]) is None
    print('Recursive OK!')


