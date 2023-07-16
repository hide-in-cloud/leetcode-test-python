"""
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = [0] * (n+1)
        for i in range(n):
            lst[nums[i]] += 1
        result = []
        for i in range(1, n+1):
            if lst[i] == 2:
                result.insert(0, i)
            elif lst[i] == 0:
                result.insert(1, i)
        return result

    def findErrorNums2(self, nums: List[int]) -> List[int]:
        """数学方法"""
        n, total = len(nums), sum(set(nums))
        return [sum(nums)-total, (1+n)*n//2-total]


if __name__ == '__main__':
    nums = [3,2,3,4,5]
    print(Solution().findErrorNums(nums))
