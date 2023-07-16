"""
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for k in [2,3,5]:
            while n % k == 0:
                n //= k
        return n == 1


if __name__ == '__main__':
    n = 8
    print(Solution().isUgly(n))
