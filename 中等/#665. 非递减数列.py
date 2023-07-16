"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]
"""
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True
        count = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                count += 1
                if count >= 2:
                    break
                if i - 1 >= 0:
                    if nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i-1]
                    else:
                        nums[i+1] = nums[i]
        return count < 2


if __name__ == '__main__':
    # nums = [4,3,2]
    # nums = [1,2,4,2,3]
    # nums = [2,3,3,2,2]
    nums = [3,4,2,3]
    print(Solution().checkPossibility(nums))
