from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell = 1
        max_profit = 0
        while sell < len(prices):
            carr_profit = prices[sell]-prices[buy]
            if prices[sell]>prices[buy]:
                max_profit = max(carr_profit,max_profit)
                print(max_profit,carr_profit)
            else:
                buy = sell
            sell +=1

        return max_profit
prices = [1,2,3,4,5,6]
s =Solution()
print(s.maxProfit(prices))        

