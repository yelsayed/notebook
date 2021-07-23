"""
Note on Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Initial Idea:
We can keep a window to denote the times for buying and selling.

We move one pointer when the prices are going up. When the prices start going
down move the tail pointer to the head pointer, calculate the profit before
doing that.

Example

   |
[7,1,3,5,6,4]
 |

1 is less than 7. So we can assume we're selling at a loss, but since the
minimum can be 0,
we don't calculate the loss (this makes sense if you think about whether or
not you own a stock
in the very beginning).

     |
[7,1,3,5,6,4]
   |

Here we have profit, we don't sell yet.

       |
[7,1,3,5,6,4]
   |

Still a profit so we don't sell.

         |
[7,1,3,5,6,4]
   |

Same.

           |
[7,1,3,5,6,4]
   |

At this point we're going down in value, which means we sell and we record
our profit.

Algorithm:
- Keep a window where the first pointer is the buy pointer, and the second
pointer is the sell pointer.
- If the current price is smaller than the last one:
    - Move the sell pointer up to the buy pointer
    - Get the current profit if > 0
- If the current price is bigger than the last one (meaning you'll buy more)
then don't do anything.

Complexity:
Time -> O(N)
Space -> O(1)
"""

import math
from typing import List


def max_profit(prices: List[int]) -> int:
    prices.append(-math.inf)
    i = 0
    j = 1
    profit = 0

    while j < len(prices):
        if prices[j - 1] > prices[j]:
            profit += max(prices[j - 1] - prices[i], 0)
            i = j
        j += 1

    return profit
