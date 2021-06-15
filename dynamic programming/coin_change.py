"""
This note is to study the Coin Change problem on LeetCode
https://leetcode.com/problems/coin-change/

The problem is to find the least amount of change given a coin purse
(with infinite coins) and an amount.

The thing that really helped me here is to break the problem down to sub
problems. Once you see that you can see a pattern form. Here is my break down
from my LeetCode solution.


coins = [1,2]
amount 6
- 111111
- 1111 2
- 111 2 2
- 2 2 2
   [   ]
    change (4) + one of the denom

amount 5
- 11111
- 111 2
- 1 2 2
   [   ]
    change (4) + one of the denom

amount 4
- 1 1 1 1
- 1 1 2
- 2 2
 [   ]
 change (2) + one of the denom

amount 3
- 1 1 1
- 1 2
 [   ]
 change (2) + one of the denom

amount 2
- 2
  []
  base case

amount 1
- 1
  []
  base case

---

-> min(change(6-2), change(6-3), change(6-4)) + 1
i.e. the amount minus each denomination

Use case:
coins = [1,2,5] amount = 11
dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
                                       i


Computational Complexity:
N -> Coin Size
M -> Amount + 1

The time complexity, since you have to keep going through the coins for each
coin -> O(M*N)
The space complexity is just the size of the DP array -> O(M)
"""

import math
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    # Initialize the array to have the first element to be 0 for the edge case
    # The last element should be amount + 1 because we'll be accessing the
    # array for each amount.
    dp = [math.inf] * (amount + 1)  # We use `inf` because we want to use `min`
    dp[0] = 0

    # For the amount that is exactly equal to the coin, we know it's 1
    for coin in coins:
        dp[coin] = 1

    # Go through the loop to amount + 1 (size of dp array)
    for i in range(1, amount + 1):
        # For each coin we should go back in the dp array and see the minimum
        # number of ways to get the change.
        for coin in coins:
            last_amount = i - coin
            if last_amount >= 0:
                dp[i] = min(dp[i], dp[last_amount] + 1)

    # In the end we just check if the last value hasn't been changed, meaning
    # there are no ways to create this value
    return dp[-1] if dp[-1] != math.inf else -1
