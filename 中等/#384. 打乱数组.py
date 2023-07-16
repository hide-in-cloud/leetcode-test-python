"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
"""
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # array = self.nums[:]
        array = self.nums.copy()
        random.shuffle(array)
        return array


# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.original = list(nums)
#
#     def reset(self) -> List[int]:
#         """
#         Resets the array to its original configuration and return it.
#         """
#         self.nums = list(self.original)
#         return self.nums
#
#     def shuffle(self) -> List[int]:
#         """
#         Returns a random shuffling of the array.
#         """
#         for i in range(len(self.nums)):
#             swap_idx = random.randrange(i, len(self.nums))
#             self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
#         return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution(nums)
    print(solution.shuffle())
    print(solution.reset())
    print(solution.shuffle())
