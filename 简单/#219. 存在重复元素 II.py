"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if len(set(nums)) == length:
            return False
        set1 = set()
        for i in range(length):
            if i > k:
                set1.remove(nums[i - k - 1])
            if nums[i] not in set1:
                set1.add(nums[i])
            else:
                return True
            print(set1)
        return False


if __name__ == '__main__':
    nums = [4,1,2,3,1,5]
    k = 3
    print(Solution().containsNearbyDuplicate(nums, k))
