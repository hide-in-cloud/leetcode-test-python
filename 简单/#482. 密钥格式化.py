"""
有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。

给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。

给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化
"""


class Solution:
    """
    def licenseKeyFormatting3(self, s: str, k: int) -> str:
        s = s.upper().split('-')
        n = len(s)
        index = 0
        while index < n:
            i = index
            while len(s[i]) > k:
                if i + 1 >= n:
                    s.append("")
                # print(s[i])
                s[i + 1] = s[i][k:] + s[i + 1]
                s[i] = s[i][:k]
                i += 1
            while i + 1 < n and len(s[index]) < k:
                # print(s[index])
                j = k - len(s[index])
                s[index] = s[index] + s[i + 1][:j]
                s[i + 1] = s[i + 1][j:]
                i += 1
            index = i + 1
        for i in range(n - 1, -1, -1):
            if s[i] == "":
                s.pop(i)
            else:
                break
        # print(s)
        return "-".join(s)
        """

    def licenseKeyFormatting2(self, s: str, k: int) -> str:
        """翻转字符串,从末尾开始遍历"""
        s = "".join(s.upper().split('-'))
        res = []
        for i in range(len(s), 0, -k):
            if i < k:
                res.insert(0, s[:i])
            else:
                res.insert(0, s[i - k:i])
        return "-".join(res)

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """翻转字符串,从末尾开始遍历,最后再翻转"""
        s = "".join(s.upper().split('-'))[::-1]
        res = []
        for i in range(0, len(s), k):
            res.append(s[i:i + k])
        return "-".join(res)[::-1]


if __name__ == '__main__':
    S = "2-5gf-3sd-Jxcv-41"
    K = 2
    print(Solution().licenseKeyFormatting3(S, K))
