# Dynamic Programming Examples

Model use cases of dynamic programming solved in Python. Credits to this
[youtube video](https://youtu.be/oBt53YbR9Kk?si=TGxWQLBuO0o8Znu3).



## Python's mutable default arguments

For memoisation, it seems natural to initialised a `memo` argument with an 
empty dictionary like this:

```python
def f(x, memo={}):
    # do something
    return 
```

Because of [the way python default arguments work](https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments)
this means the contents of `memo` are remembered across consecutive calls of 
`f`. For cases like the Fibonacci series, this is indeed an advantage, as 
`f(x)` depends exclusively on `x` in a mathematical sense and previous
computations can be reused safely.

In a case such as `canSum`, the memoisation key `x` is contextual to another
argument `arr`:

```python
def canSum(x, arr, memo={}):
    # do something
    return
```

so memoised values should not be kept across function calls. Therefore,
it is best to initialised `memo` as follows:

```python
def canSum(x, arr, memo=None):
    if memo is None:
        memo = {}
```

which guarantees a clean `memo` for each call.
