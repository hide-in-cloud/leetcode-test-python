"""
编写一段程序来查找第 n 个超级丑数。
超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。
"""
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """动态规划"""
        dp = [0] * (n + 1)  # 第i个丑数
        dp[1] = 1
        m = len(primes)
        pts = [1] * m
        for i in range(2, n + 1):
            dp[i] = min(dp[pts[k]] * primes[k] for k in range(m))
            for k in range(m):
                if dp[i] == dp[pts[k]] * primes[k]:
                    pts[k] += 1
        return dp[n]

    def nthSuperUglyNumber2(self, n: int, primes: List[int]) -> int:
        """最小堆"""
        heap = [1]  # 最小堆
        seen = {1}  # 用于去重
        for i in range(n - 1):
            num = heapq.heappop(heap)
            for k in primes:
                ugly = num * k
                if ugly not in seen:
                    seen.add(ugly)
                    heapq.heappush(heap, ugly)
        return heapq.heappop(heap)


if __name__ == '__main__':
    n = 12
    primes = [2,7,13,19]
    print(Solution().nthSuperUglyNumber(n, primes))
