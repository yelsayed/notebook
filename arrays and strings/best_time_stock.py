"""
Note on Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Initial Idea:
The solution here is kind of like finding the slope in the array.

You want to find the maximum rise

     /\
    /  \/
\  /
 \/
 [i  j]
From this above graph you can see that we want the section in the middle
marked [i, j] :D

The algorithm is:
- When iterating through when a new low is found
  then you make that the high and the low.
- If a new `low` is not found, then subtract that value with
  the value of `low`

[7,1,5,3,6,4]
 i
low = 7
high = 7
profit == 0

[7,1,5,3,6,4]
   i
low = 1
high = 1
profit == 0

[7,1,5,3,6,4]
     i
low = 1
high = 5
profit == 4

... and so on

This will take care of the case
[2,3,1]

Like a charm :D

Time -> O(N)
Space -> O(1)
"""
import math
from typing import List


def max_profit(prices: List[int]) -> int:
    low = math.inf
    _max_profit = 0

    for price in prices:
        if price < low:
            low = price

        _max_profit = max(_max_profit, price - low)

    return _max_profit
