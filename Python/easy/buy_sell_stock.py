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


-Approach 10/27/23
Checklist:
-Output max profit value
-Output the two index where max profit is possiblert
-return 0 if profit not possible

Steps:
1.
Declare object with 3 keys: buyDay, sellDay, and profit
2.
Iterate list, checking for the min and max value from left to right
3. Find the difference to get profit
4.If the number always gets smaller or stays the same, return 0
'''
# test_prices = [7, 1, 5, 3, 6, 4]
# test_prices2 = [7, 6, 4, 3, 1]
# test_prices3 = []
# test_prices4 = [7, 1, 1, 1, 1, 1]


# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 0:
#             return 0
#         res = {"buy": {"day":0, "cost":prices[0]}, "sell": {"day":0, "cost":0}, "profit": 0}
#         for i in range(0, len(prices) - 1):
#             for j in range(i+1, len(prices) - 1):
#                 if j < len(prices) - 1:
#                     if res["buy"]["cost"] > prices[j]:
#                         res["buy"]["cost"] = prices[j]
#                         res["buy"]["day"] = j
#                     if res['sell']["cost"] < prices[j]:
#                         res["sell"]["cost"] = prices[j]
#                         res["sell"]["day"] = j
#         res['profit'] = res["sell"]["cost"] - res['buy']["cost"]
#         if res['profit'] <= 0: return 0
#         if res["sell"]["day"] < res["buy"]["day"]: return 0
#         return res


# max_profit = Solution()
# print(max_profit.maxProfit(test_prices))
# print(max_profit.maxProfit(test_prices2))
# print(max_profit.maxProfit(test_prices3))
# print(max_profit.maxProfit(test_prices4))


'''
Approach 1:
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
