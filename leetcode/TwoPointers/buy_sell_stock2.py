'''
Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the
price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Link to problem:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        - I can buy and sell stocks multiple times
        - I'll need 2 pointers to compare stocks
        - I'll need a variable to track total profit

        1. Delcare l and r pointer and profit = 0
        2. while loop, while r hasn't reached the end
        if prices[r] - prices[l] > 0, then profit += prices[r] - prices[l], and l = r
        r ++ everytime
        3. return profit
        """
        l, r, total_profit = 0, 1, 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0: 
                total_profit += profit
            l += 1
            r += 1
        return total_profit
    
res = Solution()
print("Ans:", res.maxProfit([7,1,5,3,6,4]))
