"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，
如果目标值存在返回下标，否则返回 -1。
"""


class Solution:
    def search(self, nums, target) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2  # 避免溢出
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 0
    print(Solution().search(nums, target))
