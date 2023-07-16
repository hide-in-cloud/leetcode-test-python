"""
给你一个字符串 s 和一个字符串数组 dictionary 作为字典，
找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串
"""
from typing import List


class Solution:
    def findLongestWord2(self, s: str, dictionary: List[str]) -> str:
        """动态规划"""
        m = len(s)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if j + ord('a') == ord(s[i]) else f[i + 1][j]

        longestWord = ""
        for word in dictionary:
            n = len(word)
            i = 0
            index = 0
            while i < n:
                if f[index][ord(word[i]) - ord('a')] == m:
                    break
                index = f[index][ord(word[i]) - ord('a')] + 1
                i += 1
            if i == n:
                # print(word)
                if n > len(longestWord):
                    longestWord = word
                elif n == len(longestWord) and word < longestWord:  # 长度相同找字符串字典顺序最小的
                    longestWord = word
        return longestWord

    def findLongestWord2(self, s: str, dictionary: List[str]) -> str:
        """双指针"""
        m = len(s)
        longestWord = ""
        for word in dictionary:
            n = len(word)
            i = j = 0
            while i < n and j < m:
                if word[i] == s[j]:
                    i += 1
                j += 1
            if i == n:
                # print(word)
                if n > len(longestWord):
                    longestWord = word
                elif n == len(longestWord) and word < longestWord:
                    longestWord = word
        return longestWord

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        """先排序,然后用find()函数查找子序列"""
        dictionary.sort(key=lambda x: (-len(x), x))  # 先排长度,后排字符串字典顺序
        for word in dictionary:
            index = 0
            for c in word:
                index = s.find(c, index) + 1
                if not index:
                    break
            else:  # 这里用else语句保证break之后不会执行，正常循环结束会执行
                return word
        return ""


if __name__ == '__main__':
    s = "abced"
    dictionary = ["abe", "abc", "abd"]
    print(Solution().findLongestWord(s, dictionary))
