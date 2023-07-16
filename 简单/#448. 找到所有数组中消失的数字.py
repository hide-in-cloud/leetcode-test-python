"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """数学方法"""
        return list({i for i in range(1, len(nums) + 1)} - set(nums))

    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        """原地修改, 空间复杂度O(1)"""
        n = len(nums)
        for i in range(n):
            nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])  # 后面的数需要复原再修改
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res


if __name__ == '__main__':
    # nums = [1, 2, 2, 3, 1,4]
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers2(nums))
