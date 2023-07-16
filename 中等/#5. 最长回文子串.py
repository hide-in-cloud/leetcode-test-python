"""
给你一个字符串 s，找到 s 中最长的回文子串。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """利用中心扩展"""
        n = len(s)

        def expandAroundCenter(left, right):
            """中心扩展"""
            # 从中心旁边的两个字符开始判断，不断向两边扩散
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right-1

        end, start = 0, 0
        for i in range(n):
            # 以i为中心点，向两边扩展
            left1, right1 = expandAroundCenter(i, i+1)  # 长度为偶数
            left2, right2 = expandAroundCenter(i-1, i+1)  # 长度为奇数
            # 取最长的
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end+1]

    def longestPalindrome2(self, s: str) -> str:
        """动态规划"""
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        # 只有1个字符的子串肯定是回文
        for i in range(n):
            dp[i][i] = True

        max_len = 1  # 最大长度
        begin = 0  # 最终起始位置
        # 先固定子串长度L
        for L in range(2, n+1):
            # 再调整子串的起始位置i
            for i in range(n):
                # 子串的终止位置j：由j - i + 1 = L, 得j = L + i - 1
                j = L + i - 1
                # 如果右边界越界，退出当前循环
                if j >= n:
                    break
                # 头尾字符不同，不是回文
                if s[i] != s[j]:
                    dp[i][j] = False
                # 头尾字符相等
                else:
                    # 子串长度小于等于3，是回文
                    if L <= 3:
                        dp[i][j] = True
                    # 长度大于3时，取决于比它小的子串是不是回文
                    else:
                        dp[i][j] = dp[i+1][j-1]
                # 更新最大长度和起始位置
                if dp[i][j] and L > max_len:
                    max_len = L
                    begin = i
        return s[begin:begin + max_len]


if __name__ == '__main__':
    s = "caacecaatat"
    print(Solution().longestPalindrome2(s))
