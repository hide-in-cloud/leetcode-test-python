"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """双指针, O(n^2)"""
        ans = []
        n = len(nums)
        nums.sort()
        # print(nums)

        if n < 3:
            return ans

        # a <= b <= c
        for i in range(n):
            if nums[i] > 0:  # 第一个数大于0，则和一定大于0
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                while left < right and nums[left] + nums[right] < target:
                    left += 1
                while left < right and nums[left] + nums[right] > target:
                    right -= 1
                if nums[left] + nums[right] == target:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left+1 < right and nums[left+1] == nums[left]:  # 去重
                        left += 1
                    while right-1 > left and nums[right-1] == nums[right]:  # 去重
                        right -= 1
                    left += 1
                    right -= 1

        return ans

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        """双指针"""
        ans = []
        n = len(nums)
        nums.sort()
        # print(nums)

        if n < 3:
            return ans

        for i in range(n-2):  # 枚举 a
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 需要和上一次枚举的数不相同
                continue

            target = -nums[i]
            k = n-1  # c 的初始位置
            for j in range(i+1, n-1):  # 枚举 b
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                if j < k and nums[j] + nums[k] < target:
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j == k:
                    break
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])

        return ans

    def threeSum3(self, nums: List[int]) -> List[List[int]]:
        """空间换时间, 哈希表去重, ①[0,0,0] ②[-2x,x,x] ③[a,b,c]"""
        import collections
        import bisect
        ans = []
        if len(nums) < 3:
            return ans

        mp = collections.Counter(nums)
        keys = sorted(mp)
        for i, num in enumerate(keys):
            if mp[num] > 1:
                if num == 0 and mp[num] >= 3:  # 处理零
                    ans.append([0,0,0])
                elif num != 0 and -2*num in mp:  # 处理两个相同数字的情况
                    ans.append([-2*num, num, num])
            if num < 0:
                target = -num  # 两数之和
                left = bisect.bisect_left(keys, target-keys[-1], lo=i+1)  # 第二个数的起始索引
                right = bisect.bisect_right(keys, target//2, left)  # 第二个数的最大索引
                for second in keys[left:right]:
                    third = target-second
                    if third in mp and third != second:
                        ans.append([num, second, third])

        return ans


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4,0,-2,-3,3,3,0,4,4]
    # nums = [0,0,0,0]
    print(Solution().threeSum3(nums))
