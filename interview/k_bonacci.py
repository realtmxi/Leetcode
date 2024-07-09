# Nirmata AI/ML Interview Round 2 
# Date: 2024-07-09

from collections import deque

def fib(n):
    prev_1, prev_2 = 1, 1
    if n <= 1:
        return n
    for i in range(2, n):
        result = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = result

    return prev_2

def trib_recursive(n):
    """
    Calculate the n-th tribonacci number
    1, 1, 2, 4, 7, 13, 24, 44, 81, ...
    """
    if n <= 2:
        return 1
    if n == 3:
        return 2
    return trib_recursive(n - 1) + trib_recursive(n - 2) + trib_recursive(n - 3)

def trib_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

def trib_opt(n):
    prev_1, prev_2, prev_3 = 1, 1, 2
    if n <= 2:
        return 1
    if n == 3:
        return 2
    for i in range(4, n+1):
        result = prev_1 + prev_2 + prev_3
        prev_1 = prev_2
        prev_2 = prev_3
        prev_3 = result

    return prev_3

def k_bonacci(n, k):
    """
    each term is the sum of the k previous terms
    the first k element of k_bonacci sequence would be the first k element of fibonacci sequence
    k = 2, fibonacci
    k = 3, tribonacci
    """

    if n <= k:
        return fib(n)
    dp = [0] * (n + 1)
    for i in range(1, k): # O(k^2)
        dp[i] = fib(i)
    for i in range(k, n + 1): # O(nk -k^2)
        dp[i] = sum(dp[i - k:i])
    return dp[n]

def k_bonacci_opt(n, k):
    """
    deque operation:
    append
    popleft
    O(min{n-k, k^2})
    """
    if n <= k:
        return fib(n) # O(k)

    dp = deque()
    sum = 0
    for i in range(0, k): # O(k^2)
        element = fib(i)
        dp.append(element)
        sum += element

    dp.append(sum)

    for i in range(k + 1, n + 1): # from O(nk -k^2) to O(n - k)
        temp = dp.popleft()
        sum = sum * 2 - temp
        dp.append(sum)

    return sum


if __name__ == "__main__":
    for i in range(1, 10):
        print(k_bonacci_opt(i, 3))

