"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left, right):
            """中心扩展"""
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        res = 0
        for i in range(len(s)):
            res += expandAroundCenter(i, i)  # 奇数
            res += expandAroundCenter(i, i+1)  # 偶数
        return res

    def countSubstrings2(self, s: str) -> int:
        """ Manacher算法 """
        new = '$#' + '#'.join(s) + '#!'  # 回文串为奇数位 两侧不同不做越界判断
        n = len(new)  # 注意减一
        dp = [0] * n  # i为中心最大回文串半径
        # 原回文串长度dp[i]-1 总回文串长度2*dp[i]-1 #的个数一定为dp[i]
        # 最大回文串能构成回文串数 dp[i]/2
        # 以i为中心 最大回文串半径 右端点i+dp[i]-1
        center = right = 0  # 当前最大的回文右端点 以及对应的回文中心
        ans = 0
        for i in range(1, n - 1):
            if i <= right:
                dp[i] = min(right - i + 1, dp[2 * center - i])
            else:
                dp[i] = 1
            # 扩展回文串
            while new[i + dp[i]] == new[i - dp[i]]:
                dp[i] += 1
            if i + dp[i] - 1 > right:
                center = i
                right = i + dp[i] - 1
            ans += dp[i] // 2

        return ans


if __name__ == '__main__':
    s = "aaaa"
    print(Solution().countSubstrings(s))
