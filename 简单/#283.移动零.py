"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
"""
from typing import List


class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """删除0,再添加0"""
        n = len(nums)
        i = 0
        count = 0
        while i < n-count:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count += 1
            else:
                i += 1
        print(nums)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """快慢指针"""
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < n:
            nums[j] = 0
            j += 1
        print(nums)

    def moveZeroes3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """互换位置"""
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        print(nums)

    def moveZeroes4(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """sort"""
        # nums.sort(key=lambda x: x == 0)
        nums.sort(key=lambda x: x != 0, reverse=True)
        print(nums)


if __name__ == '__main__':
    nums = [0,1,0,13,12,0,6,5,0,7]
    # nums = [0]
    print(Solution().moveZeroes(nums))
