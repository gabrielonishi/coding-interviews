"""
Memoization is a technique used to store values used for what would
be redundant calculations. It sacrifices memory for speed.

In this example, the fibo functions does many redundant calculations
because we calculate both fibo(n - 1) and fibo(n - 2) subsequentely.

For example, for fibo(5), the recursion stack would look like this:

Stack:
 - fibo(4)
 - fibo(3)
 - fibo(2) #returns
 - fibo(3)
 - fibo(2) #returns

"""

import time

n = 38


def fibo(n: int) -> int:
    '''
    Returns the nth fibonacci number

    Args:
        n (int): Nth fibonacci number

    Returns:
        int: Value of nth fibonacci number
    '''

    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    return fibo(n - 1) + fibo(n - 2)


start_time = time.time()
print(fibo(n))
print(f"Time to run fibo({n}): {(time.time() - start_time):.4f}s")


memo = {
    0: 0,
    1: 1,
    2: 1
}


def fibo_memo(n: int) -> int:
    '''
    Returns the nth fibonacci number using memoization

    Args:
        n (int): Nth fibonacci number

    Returns:
        int: Value of nth fibonacci number
    '''
    if n in memo:
        return memo[n]

    ret = fibo_memo(n - 1) + fibo_memo(n - 2)

    memo[n] = ret

    return ret


start_time = time.time()
print(fibo_memo(n))
print(f"Time to run fibo({n}): {(time.time() - start_time):.4f}s")
