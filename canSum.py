"""
Determine whether a target value can be obtained from adding numbers in 
an array.

1. Array values may be used as many times as necessary

2. All input values are positive integers


"""

import time

def recursive_canSum(t, arr):
    """
    Recursive implementation. Time complexity O(m^t), where t is the target sum
    and m is len(arr).
    """
    # end cases
    if t in arr: return True
    if t < min(arr): return False

    if any(recursive_canSum(t-v, arr)  for v in arr): return True

    return False


def canSum(t, arr, memo=None):
    """
    Memoised implementation. Time complexity O(t*m).
    """
    if memo is None:  # avoid Python's mutable default arg behaviour
        memo = {}
    # end cases
    if t in memo: return memo[t]
    if t in arr: return True
    if t < min(arr): return False

    memo.update({
        t: any(canSum(t-v, arr, memo) for v in arr)
    })

    return memo[t]


def timeit(f, *args):
    tick = time.time()
    result = f(*args)
    tock = time.time()
    return (tock-tick) * 1000  # in ms


if __name__ == "__main__":
    assert recursive_canSum(7, [5, 3, 4]) is True
    assert recursive_canSum(12, [2, 8]) is True
    assert recursive_canSum(3, [4, 2, 5]) is False
    assert recursive_canSum(7, [2, 4]) is False
    print('Recursive OK!')
   
    assert canSum(7, [5, 3, 4]) is True
    assert canSum(12, [2, 8]) is True
    assert canSum(3, [4, 2, 5]) is False
    assert canSum(7, [2, 4]) is False
    print('Memoised OK!')
    # timings
    target = 200
    arr =[7, 14]
    recursive_time = timeit(recursive_canSum, target, arr)
    memoised_time = timeit(canSum, target, arr)

    print(f"Recursive {recursive_time:.2f} ms")
    print(f"Memoised {memoised_time:.2f} ms")

