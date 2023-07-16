"""
给定一个长度为 n 的 非空 整数数组，每次操作将会使 n - 1 个元素增加 1。找出让数组所有元素相等的最小操作次数。
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """其余n-1个数加1 相当于 某个数减1"""
        minNum = min(nums)
        count = 0
        for num in nums:
            count += num - minNum
        return count

    def minMoves2(self, nums: List[int]) -> int:
        """其余n-1个数加1 相当于 某个数减1"""
        return sum(nums) - min(nums) * len(nums) if len(nums) != 1 else 0

    def minMoves3(self, nums: List[int]) -> int:
        """先排序,再利用差值"""
        nums.sort()
        count = 0
        for i in range(len(nums)-1,0,-1):
            count += nums[i] - nums[0]
        return count


if __name__ == '__main__':
    nums = [1,2,3,4]  # 7,7,7,7
    print(Solution().minMoves3(nums))
