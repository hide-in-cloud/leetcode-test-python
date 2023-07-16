"""
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，
使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            if i > k:
                window.remove(nums[i - k - 1])
            window.add(nums[i])
            idx = window.bisect_left(nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window)-1 and abs(window[idx+1] - window[idx]) <= t:
                return True
            # print(window)
        return False


if __name__ == '__main__':
    nums = [4,1,2,3,1,5]
    k = 3
    t = 0
    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
