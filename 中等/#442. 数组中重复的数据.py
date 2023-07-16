"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
"""
from typing import List
import collections


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """哈希表"""
        res = []
        for num, count in collections.Counter(nums).items():
            if count == 2:
                res.append(num)
        return res

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        """对应下标的数加上n"""
        n = len(nums)
        for i in range(n):
            x = (nums[i]-1) % n
            nums[x] += n
        return [i+1 for i in range(n) if nums[i] > 2*n]

    def findDuplicates3(self, nums: List[int]) -> List[int]:
        """对应下标的数取反"""
        n = len(nums)
        res = []
        for i in range(n):
            j = abs(nums[i])-1  # 原数组对应下标
            if nums[j] < 0:  # 负数说明是出现的第二次
                res.append(j + 1)
            else:
                nums[j] *= -1
        return res


if __name__ == '__main__':
    # nums = [1, 2, 2, 3, 1,4]
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDuplicates3(nums))
