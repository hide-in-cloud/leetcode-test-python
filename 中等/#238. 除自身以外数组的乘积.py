"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
"""
from typing import List


class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p_left = [0] * n
        p_left[0] = 1
        p_right = [0] * n
        p_right[n-1] = 1
        ans = [0] * n

        # L[i] 为索引 i 左侧所有元素的乘积
        for i in range(1, n):
            p_left[i] = p_left[i-1] * nums[i-1]
        # R[i] 为索引 j 右侧所有元素的乘积
        for j in range(n-2, -1, -1):
            p_right[j] = p_right[j+1] * nums[j+1]

        for i in range(n):
            ans[i] = p_left[i] * p_right[i]
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1

        # L[i] 为索引 i 左侧所有元素的乘积
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        R = 1  # 当前索引右侧所有元素的乘积
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * R
            R = R * nums[i]  # 下一个索引的乘积

        return ans


if __name__ == '__main__':
    nums = [1,2,3,4]
    # nums = [-1,1,0,-3,3]
    print(Solution().productExceptSelf(nums))
