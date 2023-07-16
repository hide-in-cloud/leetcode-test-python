"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
"""

import collections


def frequencySort(s: str) -> str:
    """使用Counter类,按value排序,O(n+klogk)"""
    ans = ""
    dic = collections.Counter(s)
    sorted_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    for k, v in sorted_dic:
        ans += k*v
    return ans


def frequencySort2(s: str) -> str:
    """使用Counter类的most_common()方法,获取频率最高的前n个"""
    dic = collections.Counter(s)
    return "".join(k*v for k, v in dic.most_common())


def frequencySort3(s: str) -> str:
    """桶排序,O(n+k)"""
    ans = ""
    dic = collections.Counter(s)  # 统计频次
    max_freq = max(dic.values())  # 最大频次
    bucket = [""] * (max_freq+1)  # 创建桶
    for ch, num in dic.items():  # 对于1~max_freq的每个频次的字符分别加入桶
        bucket[num] += ch
    # print(bucket)
    for i in range(max_freq, 0, -1):  # 按照出现频率从大到小的顺序遍历桶
        for ch in bucket[i]:
            ans += ch*i
    return ans


def frequencySort4(s: str) -> str:
    """散列表+堆排序"""
    import heapq
    ans = ""
    dic = collections.Counter(s)  # 统计频次
    max_heap = []  # 最大堆
    for ch, num in dic.items():  # 根据频次使用堆排序
        heapq.heappush(max_heap, (num,ch))
    # print(max_heap)
    while max_heap:
        item = heapq.heappop(max_heap)
        ans += item[0] * item[1]
    return ans[::-1]


if __name__ == '__main__':
    s = "cdAabbcbdeebd"
    # s = "tree"
    print(frequencySort4(s))

