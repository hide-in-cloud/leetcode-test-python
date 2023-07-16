"""
给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。
但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，
并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号
"""
from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        ans = str(nums[0]) + "/(" + str(nums[1])
        for i in range(2, n):
            ans += "/" + str(nums[i])
        return ans + ")"


if __name__ == '__main__':
    nums = [5,20,50,10,100,1000,5,20,10,2]
    # nums = [5,20,2]
    print(Solution().optimalDivision(nums))
