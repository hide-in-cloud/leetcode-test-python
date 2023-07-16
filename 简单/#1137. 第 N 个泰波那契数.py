"""
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for i in range(n):
            a, b, c = b, c, a+b+c
        return a

    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        T = [0] * (n + 1)
        T[0], T[1], T[2] = 0, 1, 1
        for i in range(3, n + 1):
            T[i] = T[i - 3] + T[i - 2] + T[i - 1]
        return T[n]


if __name__ == '__main__':
    n = 1
    print(Solution().tribonacci(n))
