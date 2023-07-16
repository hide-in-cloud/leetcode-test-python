"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""
from math import gcd
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """旋转数组"""
        n = len(nums)
        k %= n
        nums[::] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        print(nums)

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """环状置换"""
        n = len(nums)
        k %= n
        count = gcd(k, n)
        for start in range(count):
            current = start
            buffer = nums[start]
            while True:
                nextIndex = (current + k) % n
                buffer, nums[nextIndex] = nums[nextIndex], buffer
                current = nextIndex
                if current == start:
                    break
        print(nums)

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """旋转数组"""
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)

    def rotate3(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ pop and insert """
        k %= len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())
        print(nums)

    def rotate4(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ 额外空间 """
        n = len(nums)
        k %= n
        res = [0]*n
        for i in range(n):
            res[(i+k) % n] = nums[i]
        nums[:] = res
        print(nums)

    def rotate5(self, nums: List[int], k: int) -> None:
        """置换"""
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 10
    print(Solution().rotate1(nums, k))
