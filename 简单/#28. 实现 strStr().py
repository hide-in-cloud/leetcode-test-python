"""
实现 strStr() 函数。

给你两个字符串 haystack 和 needle，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr2(self, haystack: str, needle: str) -> int:
        """暴力算法"""
        if needle == "":
            return 0

        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr3(self, haystack: str, needle: str) -> int:
        """KMP算法"""
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        #  根据模式串构造next数组
        next = [0] * m
        k = 0
        next[0] = k
        for i in range(1, m):
            while k > 0 and needle[i] != needle[k]:
                k = next[k - 1]
            if needle[i] == needle[k]:
                k += 1
            next[i] = k
        # print(next)

        # 原串与模式串匹配
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1


if __name__ == '__main__':
    haystack = "aaaabaaabc"
    needle = "aaabc"
    print(Solution().strStr3(haystack, needle))
