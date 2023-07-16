"""
给你两个字符串，请你从这两个字符串中找出最长的特殊序列。

「最长特殊序列」定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。
子序列 可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。
输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1
"""
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """先按字符长度和字典顺序排序,再找出唯一出现的字符串，再看它是否是其他字符串的子序列"""
        strs.sort(key=lambda x: (-len(x), x))
        # print(strs)
        for i in range(len(strs)):
            if i+1 == len(strs) or strs[i] != strs[i+1]:
                # 从排在该字符串前面的字符串里判断是否特殊
                j = 0
                while j < i:
                    if self.isSubsequence(strs[i], strs[j]):
                        break
                    else:
                        j += 1
                if j == i:
                    return len(strs[i])
        return -1

    def isSubsequence(self, s: str, t: str) -> bool:
        """利用好find()函数"""
        index = 0
        for c in s:
            index = t.find(c, index) + 1
            if not index:
                return False
        return True


if __name__ == '__main__':
    # strs = ["a","b","c","d","e","f","a","b","c","d","e","f"]
    strs = ["aaa","aaa","aa","a","bb","b"]
    print(Solution().findLUSlength(strs))
