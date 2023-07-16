"""
给定一个长度为 n 的整数数组 A 。

假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。

计算F(0), F(1), ..., F(n-1)中的最大值。
"""
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        数组逆转跟乘数逆转是一样的
        4     3     2     6
        0*4   1*3   2*2   3*6   F(0)
        1*4   2*3   3*2   0*6   F(1) = F(0) + SUM(data) - N * data[3];
        2*4   3*3   0*2   1*6   F(2) = F(1) + SUM(data) - N * data[2];
        3*4   0*3   1*2   2*6   F(3) = F(2) + SUM(data) - N * data[1];
        可得出 F(i+1) = F(i) + sumA - nA[n-i-1]
        """
        n = len(nums)
        sum_nums = sum(nums)
        f = 0
        for i in range(n):
            f += i * nums[i]
        max_f = f
        for i in range(1, n):
            f = f + sum_nums - n * nums[n-i]
            # print(f)
            max_f = max(max_f, f)
        return max_f


if __name__ == '__main__':
    # A = [4, 3, 2, 6]
    A = [18,4,13,-1,2,7,19,14,11,0,-9,9,4,2,-2,-7,18,18,-7,-5,9,6,-8,3,13,0,15,9,10,-1]
    print(Solution().maxRotateFunction(A))
