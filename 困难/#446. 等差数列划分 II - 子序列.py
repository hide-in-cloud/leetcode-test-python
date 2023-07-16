"""
给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。

如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该序列为等差序列。

例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
再例如，[1, 1, 2, 5, 7] 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。

例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
题目数据保证答案是一个 32-bit 整数
"""
from typing import List
import collections


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # 以 nums[i]为结尾，公差为d的子序列的个数
        dp = [collections.defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]
                if d in dp[i]:
                    dp[i][d] += 1
                else:
                    dp[i][d] = 1
                if d in dp[j]:
                    # dp[i]可以加到所有以dp[j]结尾的公差为d的数列后面
                    dp[i][d] += dp[j][d]
                    ans += dp[j][d]
        return ans


if __name__ == '__main__':
    nums = [2,4,6,8,10,12,14,15,16,17]
    print(Solution().numberOfArithmeticSlices(nums))
