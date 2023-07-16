"""
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
"""
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """哈希表,记录 {每个元素:[出现的频次,第一次出现的位置,最后一次出现的位置]} """
        mp = {}  # num: [count, start, end]
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = [1, i, i]
            else:
                mp[num][0] += 1
                mp[num][2] = i
        # print(mp)
        degree = max(mp.values(), key=lambda x: x[0])[0]
        res = len(nums)
        for v in mp.values():
            if v[0] == degree:
                res = min(res, v[2] - v[1] + 1)
        return res

    def findShortestSubArray2(self, nums: List[int]) -> int:
        mp = {}  # num: [count, start, end]
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = [1, i, i]
            else:
                mp[num][0] += 1
                mp[num][2] = i
        # print(mp)
        max_count, min_len = 0, len(nums)
        for count, start, end in mp.values():
            if count > max_count:
                max_count = count
                min_len = end - start + 1
            elif count == max_count:
                min_len = min(min_len, end - start + 1)
        return min_len


if __name__ == '__main__':
    # nums = [1, 2, 2, 3, 1,4]
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(Solution().findShortestSubArray2(nums))
