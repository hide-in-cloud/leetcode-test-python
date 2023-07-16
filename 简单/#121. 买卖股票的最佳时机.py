"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """贪心"""
        min_left = prices[0]
        max_profit = 0
        for num in prices:
            min_left = min(min_left, num)
            max_profit = max(max_profit, num - min_left)
        return max_profit

    def maxProfit2(self, prices: List[int]) -> int:
        """动态规划"""
        n = len(prices)
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i] - min_price)
        return max(dp)

    def maxProfit3(self, prices: List[int]) -> int:
        """分治"""
        n = len(prices)
        if n == 1:
            return 0  # 不存在差值
        mid = n >> 1
        prices_left = prices[:mid]
        prices_right = prices[mid:]
        left = self.maxProfit3(prices_left)
        right = self.maxProfit3(prices_right)
        left_right = max(prices_right) - min(prices_left)
        return max(left, right, left_right)

    def maxProfit4(self, prices: List[int]) -> int:
        """暴力, 超时"""
        n = len(prices)
        maxProfit = 0
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] - prices[i] > maxProfit:
                    maxProfit = prices[j] - prices[i]
        return maxProfit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    print(Solution().maxProfit(prices))
