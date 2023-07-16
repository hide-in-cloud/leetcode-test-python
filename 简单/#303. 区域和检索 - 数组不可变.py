"""
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums
        for num in nums:
            _sums.append(_sums[-1] + num)
        # print(self.sums)

    def sumRange(self, left: int, right: int) -> int:
        _sums = self.sums
        return _sums[right+1] - _sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    left, right = 2, 5
    print(NumArray(nums).sumRange(left, right))
