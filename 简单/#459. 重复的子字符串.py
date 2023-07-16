"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000
"""
import collections


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """利用重复字符串的特性"""
        return (s+s).find(s, 1) != len(s)

    def repeatedSubstringPattern2(self, s: str) -> bool:
        """优化的暴力算法"""
        n = len(s)
        for i in range(1, n//2+1):  # i为子字符串的长度
            if n % i == 0:
                if all(s[j-i:j] == s[j:j+i] for j in range(i,n,i)):
                    return True
        return False


if __name__ == '__main__':
    s = "abcabc"
    print(Solution().repeatedSubstringPattern(s))
