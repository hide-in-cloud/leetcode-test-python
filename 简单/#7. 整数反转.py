"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）
"""


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            num = num * 10 + x % 10
            x = x // 10
        if -2**31 <= sign * num <= 2**31-1:
            return sign * num
        else:
            return 0


if __name__ == '__main__':
    x = -123
    # x = 120
    print(Solution().reverse(x))
