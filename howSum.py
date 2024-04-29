"""
Given an array of numbers, determine subset which adds up exactly to the
target  sum.

1. Assume all numbers are positive integers

2. If no subset can be found return None

"""

from canSum import timeit


def recursive_howSum(t, arr):
    """
    Recursive implementation.
    Time complexity:
        List extension operation: O(k), where len(list) = k. Worst case: k = t.
        Recursive calls: O(m^t) where len(arr) = m.
        Total: O(m^t * t)

    """
    if t == 0: return []
    if t < min(arr): return None

    for v in arr:
        result = recursive_howSum(t-v, arr)
        if result != None:
            return  result + [v]  # list extension has complexity O(k)
    
    return None


def howSum(t, arr, memo=None):
    """
    Memoised implementation. O(m * t^2).

    """
    if memo == None:
        memo = {}
    if t in memo: return memo[t]
    if t == 0: return []
    if t < min(arr): return None

    for v in arr:
        result = howSum(t-v, arr, memo)
        memo.update({
            t-v: result
        })
        if result != None:
            return  result + [v]  

    return None



if __name__ == '__main__':
    assert recursive_howSum(7, [5, 3, 7]) == [7]
    assert set(recursive_howSum(7, [4, 3])) == set([3, 4])
    assert recursive_howSum(7, [5, 3]) is None
    print("Recursive OK!")

    assert howSum(7, [5, 3, 7]) == [7]
    assert set(howSum(7, [4, 3])) == set([3, 4])
    assert howSum(7, [5, 3]) is None
    print("Memoised OK!")

    # timings
    target = 200
    recursive_time = timeit(recursive_howSum, target, [7, 14])
    memoised_time = timeit(howSum, target, [7, 14])
    print(f"Recursive {recursive_time:.2f} ms")
    print(f"Memoised {memoised_time:.2f} ms")




