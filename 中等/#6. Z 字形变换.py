"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串
"""


class Solution:

    def convert2(self, s: str, numRows: int) -> str:
        """根据Z型索引查找每一行索引的规律"""
        if numRows == 1:
            return s

        strs = [""] * numRows
        row = 0
        for i in range(len(s)):
            k = i % (2 * numRows - 2)
            if k <= numRows - 1:
                row = k
            elif k > numRows - 1:
                row = 2 * numRows - 2 - k
            strs[row] += s[i]
        # for str in strs:
        #     print(str)
        return "".join(strs)

    def convert(self, s: str, numRows: int) -> str:
        """按行排序,跟踪索引"""
        if numRows == 1:
            return s

        strs = [""] * numRows
        row = 0
        goingDown = False
        for c in s:
            strs[row] += c
            if row == 0 or row == numRows - 1:
                goingDown = not goingDown
            row += 1 if goingDown else -1
        # for str in strs:
        #     print(str)
        return "".join(strs)


if __name__ == '__main__':
    s = "ABCDEFGHIJK"
    numRows = 3
    print(Solution().convert(s, numRows))
