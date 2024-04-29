"""
Determine whehter a target string can be built from an array of strings.

"""

from canSum import timeit

def recursive_canConstruct(t, arr):
    """
    Complexity: O(m * n^m)
    Recursive calls: O(n^m); where len(t) = m and len(arr) = n.
    String slicing: O(k); where k is len(string).

    """

    if t == '': return True  # consumed whole target
    
    for word in arr:
        if t.startswith(word):  # check if word is prefix
            remainder = t[len(word):]  # consume from beginning
            if recursive_canConstruct(remainder, arr):
                return True

    # tried every word, return False
    return False

def canConstruct(t, arr, memo=None):
    """
    Complexity: m * n * m
    
    """
    if memo is None:
        memo={'': True}

    if t in memo: return memo[t]

    for word in arr:
        if t.startswith(word):
            remainder = t[len(word):]
            if canConstruct(remainder, arr, memo):
                memo.update({
                    remainder: True
                })
                return True

    memo.update({t: False})
    return memo[t]
    


if __name__ == '__main__':
    # recursive
    assert recursive_canConstruct(
        'abcdef',
        ['ab', 'abc', 'cd', 'def', 'abcd']
    ) is True
    assert recursive_canConstruct(
        'abcd',
        ['ab', 'cde', 'cdef', 'bc']
    ) is False
    
    # memoised
    assert canConstruct(
        'abcdef',
        ['ab', 'abc', 'cd', 'def', 'abcd']
    ) is True
    assert canConstruct(
        'abcd',
        ['ab', 'cde', 'cdef', 'bc']
    ) is False

    # timings
    rec = timeit(
        recursive_canConstruct,
        'eeeeeeeeeeeeeef',
        ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeeee']
    )
    mem = timeit(
        canConstruct,
        'eeeeeeeeeeeeeef',
        ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeeee']
    )

    print(f"Recursive: {rec:.2f} ms")
    print(f"Memoised: {mem:.2f} ms")
