"""
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """贪心"""
        total_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                total_profit += profit
        return total_profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))
