"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        res = ""
        i = 0
        c = 0  # 进位标志
        while i < n or i < m:
            c += ord(num1[n - 1 - i]) - ord('0') if i < n else 0
            c += ord(num2[m - 1 - i]) - ord('0') if i < m else 0
            res = str(c % 10) + res
            c = c // 10
            i += 1
        if c > 0:
            res = '1' + res
        return res


if __name__ == '__main__':
    num1 = "123"
    num2 = "11"
    print(Solution().addStrings(num1, num2))
