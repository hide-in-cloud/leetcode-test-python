"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """动态规划"""

        def matches(i, j):
            if i == 0:
                return False
            if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                return True
            else:
                return False

        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True  # 两个都为空字符串
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

    def isMatch2(self, s: str, p: str) -> bool:
        if p == s:
            return True
        n, m = len(s), len(p)
        i = j = 0
        while i < n and j < m:
            if m - j >= 2 and p[j + 1] == "*":
                while i < n and (s[i] == p[j] or p[j] == "."):
                    i += 1
                j += 2
            elif s[i] == p[j] or p[j] == ".":
                i += 1
                j += 1
            else:
                return False
        if i < n:
            return False
        else:
            if "*" not in p:
                return False
            k = j
            i, j = n - 1, m - 1
            while i >= 0 and j >= k:
                if s[i] == p[j] or p[j] == ".":
                    i -= 1
                    j -= 1
                elif j >= k and p[j] == "*":
                    while i > 0 and (s[i] == p[j - 1] or p[j - 1] == "."):
                        i -= 1
                    j -= 2
                else:
                    return False
            return True


if __name__ == '__main__':
    # s = "mississippi"
    # p = "miss.*pi"
    s = "aaa"
    p = "ac*ab*a"
    # s = "aaaa"
    # p = "aaaaa"
    print(Solution().isMatch(s, p))
