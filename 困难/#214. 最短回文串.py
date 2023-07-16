"""
给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """原字符串 + '#' + 翻转字符串, 找出最长公共前后缀"""
        def kmp(pattern: str):
            """KMP算法"""
            n = len(pattern)
            _next = [0] * n
            j = 0
            for i in range(1, n):  # s作为模式串
                while j > 0 and pattern[i] != pattern[j]:
                    j = _next[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                _next[i] = j
            return _next[-1]

        reversed_s = s[::-1]
        pattern = s + '#' + reversed_s  # "#"号分割

        return reversed_s[:len(s) - kmp(pattern)] + s

    def shortestPalindrome2(self, s: str) -> str:
        """右指针从末尾开始遍历找到最长的回文串"""
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] != s[right]:
                right -= 1
            end = right + 1
            if s[left:end][::-1] == s[left:end]:
                return s[end:][::-1] + s
            else:
                right -= 1
        return s[1:][::-1] + s

    def shortestPalindrome3(self, s: str) -> str:
        """先翻转字符串,提高效率"""
        reversed_s = s[::-1]
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            while left < right and reversed_s[left] != s[0]:
                left += 1
            if reversed_s[left:] == s[:n - left]:
                return reversed_s[:left] + s
            else:
                left += 1
        return reversed_s[:n - 1] + s


if __name__ == '__main__':
    # s = "acecaac"
    s = "abbacd"
    # s = "abcd"
    print(Solution().shortestPalindrome(s))
