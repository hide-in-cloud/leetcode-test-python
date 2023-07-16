"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """置换"""
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print(nums)
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

    def firstMissingPositive2(self, nums: List[int]) -> int:
        """标记法"""
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1
        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num-1] = -abs(nums[num-1])
        for i in range(n):
            if nums[i] >= 1:
                return i + 1
        return n + 1

    def firstMissingPositive3(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, 2**31):
            if i not in nums:
                return i


if __name__ == '__main__':
    nums = [3,4,-1,1,-2]
    # nums = [4, 3, 9, 7, 8, 2, 10, 1]
    print(Solution().firstMissingPositive3(nums))
