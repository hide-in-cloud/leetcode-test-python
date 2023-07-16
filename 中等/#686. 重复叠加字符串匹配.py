"""
给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"
"""
import collections


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """只需要检查B是否是A*k,和A*(k+1)的子串"""
        if b == "":
            return 0
        if b in a:
            return 1
        if set(b)-set(a):
            return -1
        n = len(a)
        m = len(b)
        k = m // n if m % n == 0 else m // n + 1
        for i in range(k, k+2):
            if b in a*i:
                return i
        return -1


if __name__ == '__main__':
    a = "abababaaba"
    b = "aabaaba"
    # a = "baa"
    # b = "abaab"
    print(Solution().repeatedStringMatch(a, b))
