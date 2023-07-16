"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
"""
import collections


def isAnagram(s: str, t: str) -> bool:
    """使用Counter类，最快"""
    c1 = collections.Counter(s)
    c2 = collections.Counter(t)
    if c1 == c2:
        return True
    else:
        return False


def isAnagram2(s: str, t: str) -> bool:
    """计数法"""
    if len(s) != len(t):
        return False

    cnt = [0] * 26
    for ch in s:
        cnt[ord(ch) - ord('a')] += 1
    for ch in t:
        cnt[ord(ch) - ord('a')] -= 1
        if cnt[ord(ch) - ord('a')] < 0:
            return False
    return True


def isAnagram3(s: str, t: str) -> bool:
    """排序法"""
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram2(s, t))
