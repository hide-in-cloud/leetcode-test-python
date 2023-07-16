"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """排序 + 双指针"""
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i + 1, n - 1):
                while k < n and nums[k] < nums[i] + nums[j]:
                    k += 1
                count += k - 1 - j
        return count

    def triangleNumber1(self, nums: List[int]) -> int:
        """排序 + 暴力, 超时"""
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                temp = nums[i] + nums[j]
                for k in range(j + 1, n):
                    if nums[k] < temp:
                        count += 1
                    else:
                        break
        return count

    def triangleNumber2(self, nums: List[int]) -> int:
        """排序 + 二分"""
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                a, b = nums[i], nums[j]
                if a + b > nums[-1]:
                    count += n - 1 - j
                else:
                    # 二分查找最大的满足条件的索引
                    left, right, k = j + 1, n - 1, j
                    while left <= right:
                        mid = (left + right) // 2
                        if nums[mid] < a + b:
                            k = mid
                            left = mid + 1
                        else:
                            right = mid - 1
                    count += k - j
        return count


if __name__ == '__main__':
    # nums = [2,2,3,4]
    nums = [2, 3, 4, 5, 6, 7, 8, 9]
    print(Solution().triangleNumber(nums))
