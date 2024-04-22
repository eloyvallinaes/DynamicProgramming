"""
Efficiently count the number of routs in which we can traverse an m-by-n 2D
grids where only right and down moves are allowed.

"""

import time

def recursive_gridTraveller(m, n):
    """
    Brute-force implementation. This is *slow*, with time complexity
    O(2^(m+n))

    """
    # trivial cases
    if m == 0 or n == 0: return 0  # no grid, not routes
    if m == 1 or n == 1: return 1  # only one route

    # count subtrees going down plus subtrees going right
    return recursive_gridTraveller(m-1, n) + recursive_gridTraveller(m, n-1)


def gridTraveller(m, n, memo = {}):
    """
    Memoised version. This runs in O(m * n).
    """
    m, n = sorted((m, n))  # (m, n) === (n, m)
    # trivial cases
    if m == 0 or n == 0: return 0  # no grid, not routes
    if m == 1 or n == 1: return 1  # only one route
    # result in memo
    if (m, n) in memo: return memo[(m, n)] 

    memo.update({
        (m, n): gridTraveller(m - 1, n, memo) + gridTraveller(m, n-1, memo)
    })

    return memo[(m, n)]



if __name__ == "__main__":
    assert recursive_gridTraveller(0, 1) == 0
    assert recursive_gridTraveller(1, 1) == 1
    assert recursive_gridTraveller(2, 3) == 3
    assert recursive_gridTraveller(3, 3) == 6

    # recursive call
    tic = time.time()
    routes = recursive_gridTraveller(12, 12)
    toc = time.time()
    print(f"Recursive 12x12 grid: {routes} routes in {(toc-tic)*1000:.2f} ms")

    # memoised call
    tic = time.time()
    routes = gridTraveller(12, 12)
    toc = time.time()
    print(f"Memoised 12x12 grid: {routes} routes in {(toc-tic)*1000:.2f} ms")
