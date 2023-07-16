"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）

进阶：
如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """利用好find()函数"""
        index = 0
        for c in s:
            index = t.find(c, index) + 1
            if not index:
                return False
        return True

    def isSubsequence2(self, s: str, t: str) -> bool:
        """双指针"""
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

    def isSubsequence3(self, s: str, t: str) -> bool:
        """动态规划"""
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m-1,-1,-1):
            for j in range(26):
                f[i][j] = i if j + ord('a') == ord(t[i]) else f[i+1][j]

        index = 0
        for i in range(n):
            if f[index][ord(s[i]) - ord('a')] == m:
                return False
            index = f[index][ord(s[i]) - ord('a')] + 1
        return True


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdcd"
    print(Solution().isSubsequence(s, t))
