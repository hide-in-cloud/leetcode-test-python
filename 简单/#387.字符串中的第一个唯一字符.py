"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""
import collections


def firstUniqChar(s: str) -> int:
    """使用哈希表映射"""
    d = dict()
    n = len(s)
    for i, char in enumerate(s):
        if char in d:
            d[char] = -1
        else:
            d[char] = i
    first = n
    for pos in d.values():
        if pos != -1 and pos < first:
            first = pos
    if first == n:
        return -1
    return first


def firstUniqChar2(s: str) -> int:
    """使用Counter哈希映射"""
    d = collections.Counter(s)
    for i, char in enumerate(s):
        if d[char] == 1:
            return i
    return -1


def firstUniqChar3(s: str) -> int:
    """字符第一次出现的位置与最后一次出现的位置相同"""
    for i, char in enumerate(s):
        if s.index(char) == s.rindex(char):
            return i
    return -1


def firstUniqChar4(s: str) -> int:
    min_index = len(s)
    s2 = set(s)  # set集合是无序的
    for e in s2:
        if s.find(e) != -1 and s.find(e) == s.rfind(e):
            min_index = min(s.find(e), min_index)
    return min_index if min_index < len(s) else -1


if __name__ == '__main__':
    s = "loveleetcode"
    # s = "leetcode"
    print(firstUniqChar4(s))
