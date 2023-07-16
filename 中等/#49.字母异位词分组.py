"""
给定一个字符串数组，将字母异位词组合在一起。可以按任意顺序返回结果列表。
字母异位词指字母相同，但排列不同的字符串。
"""
import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """以排序后的字符串作为标志分组的哈希表"""
    dic = collections.defaultdict(list)  # 创建一个默认值类型为列表的字典
    for s in strs:
        # print(sorted(s))
        key = "".join(sorted(s))  # 每组的标志
        dic[key].append(s)
    return list(dic.values())


def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    """以字符串的计数作为标志分组的哈希表"""
    dic = collections.defaultdict(list)
    for s in strs:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1  # 计算字符频次
        dic[tuple(cnt)].append(s)
    return list(dic.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["a"]
    # strs = ["","b",""]
    print(groupAnagrams2(strs))
