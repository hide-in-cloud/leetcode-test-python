"""
给你两个版本号 version1 和 version2 ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。
每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。
例如，2.5.33 和 0.1 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。
也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。
例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。

返回规则如下：
    如果 version1 > version2 返回 1，
    如果 version1 < version2 返回 -1，
    除此之外返回 0
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """分组后比较"""
        version1 = version1.split('.')
        version2 = version2.split('.')
        len1, len2 = len(version1), len(version2)

        for i in range(max(len1, len2)):
            a = int(version1[i]) if i < len1 else 0
            b = int(version2[i]) if i < len2 else 0
            if a != b:
                return 1 if a > b else -1
        return 0

    def compareVersion2(self, version1: str, version2: str) -> int:
        """原地比较"""
        p1 = p2 = 0
        len1, len2 = len(version1), len(version2)

        while p1 < len1 or p2 < len2:
            a, p1 = self.get_next_chunk(version1, len1, p1)
            b, p2 = self.get_next_chunk(version2, len2, p2)
            if a != b:
                return 1 if a > b else -1

        return 0

    def get_next_chunk(self, version: str, n: int, p: int):
        """获取version下一组块的号码和下标"""
        if p >= n:
            return 0, p

        p_end = p
        while p_end < n and version[p_end] != '.':
            p_end += 1
        num = int(version[p:p_end]) if p_end < n else int(version[p:n])
        p = p_end + 1

        return num, p


if __name__ == '__main__':
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    print(Solution().compareVersion2(version1, version2))
