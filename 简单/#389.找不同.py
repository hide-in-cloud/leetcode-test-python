"""
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。
"""
import collections
from functools import reduce
from operator import xor


class Solution:
    def findTheDifference4(self, s: str, t: str) -> str:
        """利用Counter类的差集实现"""
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        return (c2-c1).popitem()[0]

    def findTheDifference2(self, s: str, t: str) -> str:
        """计数法"""
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        for ch in t:
            cnt[ord(ch) - ord('a')] -= 1
            if cnt[ord(ch) - ord('a')] < 0:
                return ch
        return ''

    def findTheDifference3(self, s: str, t: str) -> str:
        """ASCII码求和法"""
        ascii_s, ascii_t = 0, 0
        for ch in s:
            ascii_s += ord(ch)
        for ch in t:
            ascii_t += ord(ch)
        return chr(ascii_t-ascii_s)  # 两者的差值即被添加的字符

    def findTheDifference(self, s: str, t: str) -> str:
        """数字相异或法"""
        # ans = 0
        # for i in s + t:
        #     ans ^= ord(i)
        # return chr(ans)

        return chr(reduce(xor, map(ord, s+t)))


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))
