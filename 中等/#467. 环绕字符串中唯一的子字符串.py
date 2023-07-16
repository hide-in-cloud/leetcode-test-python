"""
把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，
所以 s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 
现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，
尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同的非空子串的数目
"""
import collections


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        mp = collections.defaultdict(int)
        mp[p[0]] = 1
        w = 1
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i]) - ord(p[i - 1]) == -25:
                w += 1
            else:
                w = 1
            mp[p[i]] = max(mp[p[i]], w)
        return sum(mp.values())


if __name__ == '__main__':
    # p = "abcd"
    # p = "zab"
    # p = "abaab"
    p = "a"
    print(Solution().findSubstringInWraproundString(p))
