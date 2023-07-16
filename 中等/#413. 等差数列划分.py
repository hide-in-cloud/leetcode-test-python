"""
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        pre = nums[1] - nums[0]  # 前一组差
        m = 0  # 增加的子数组数量
        ans = 0
        for i in range(2, n):
            if nums[i] - nums[i-1] == pre:
                m += 1
                ans += m
            else:
                pre = nums[i] - nums[i-1]
                m = 0
        return ans


if __name__ == '__main__':
    nums = [2,4,6,8,10,14,15,16,17]
    print(Solution().numberOfArithmeticSlices(nums))
