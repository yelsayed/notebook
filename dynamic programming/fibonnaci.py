# Note to study fibbonaci using dp array rather than recursion

def fib(n):
    dp = [0, 1]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1] + dp[n - 2]

# Fib 4 can be computed by fib 3 and fib 2 which both rely on fib 1
# You can create an array with [0, 1, 0, 0, 0] (for fib 0, fib 1, fib 2, fib 3,
# fib 4) that will be updated iteratively when there is an additional fib that
# is computed.

# Simple note I guess
