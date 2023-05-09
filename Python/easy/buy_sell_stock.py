'''
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a 
given stock on the ith day.

You want to maximize your profit by choosing a single day to buy 
one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Link to problem:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Approach:
O(n) time 
O(1) space

Steps:
1.
check len(prices)
2.
Assign buy_stock=0, sell_stock=1 and max_prof=0 variables
3.
Iterate through through prices until sell stock reaches length
4.
Set current_price to selling stock - buying stock
5.
if buy is less than sell, find max between last max_profit and current profit.
else, set buy to sell
6.
return max_profit

'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0

        buying_stock_pointer, max_profit = 0, 0
        for selling_stock_pointer in range(1, len(prices)):
            current_profit = prices[selling_stock_pointer] - prices[buying_stock_pointer]
            if prices[buying_stock_pointer] < prices[selling_stock_pointer]:
                max_profit = max(current_profit, max_profit)
            else:
                buying_stock_pointer = selling_stock_pointer
        return max_profit

test_prices = [7, 1, 5, 3, 6, 4]
test_prices2 = [7, 6, 4, 3, 1]
test_prices3 = []
test_prices4 = [7, 1, 1, 1, 1, 1]
max_profit = Solution()
print(max_profit.maxProfit(test_prices))
print(max_profit.maxProfit(test_prices2))
print(max_profit.maxProfit(test_prices3))
print(max_profit.maxProfit(test_prices4))



