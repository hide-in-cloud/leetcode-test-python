"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数
"""
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """动态规划"""
        dp = [0] * (n+1)  # 第i个丑数
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n+1):
            num2, num3, num5 = dp[p2]*2, dp[p3]*3, dp[p5]*5
            dp[i] = min(num2, num3, num5)
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]

    def nthUglyNumber2(self, n: int) -> int:
        """最小堆"""
        primes = [2,3,5]
        heap = [1]  # 最小堆
        seen = {1}  # 用于去重
        for i in range(n-1):
            num = heapq.heappop(heap)
            for k in primes:
                ugly = num * k
                if ugly not in seen:
                    seen.add(ugly)
                    heapq.heappush(heap, ugly)
        return heapq.heappop(heap)


if __name__ == '__main__':
    n = 10
    print(Solution().nthUglyNumber(n))
