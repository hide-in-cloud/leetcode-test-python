"""
给定一个二进制数组， 计算其中最大连续 1 的个数。
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = count = 0
        for k in nums:
            if k == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        return max(maxCount, count)

    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        return max(map(len, "".join(map(str, nums)).split('0')))


if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))
