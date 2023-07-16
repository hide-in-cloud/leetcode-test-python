"""
给定一组字符，使用原地算法将其压缩。
压缩后的长度必须始终小于或等于原数组长度。
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
在完成原地修改输入数组后，返回数组的新长度
"""
from typing import List


class Solution:
    def compress1(self, chars: List[str]) -> int:
        """三指针原地压缩"""
        anchor = 0  # anchor指向当前读到连续字符串的起始位置
        write = 0  # 指向要写入数组的位置
        for read, ch in enumerate(chars):  # read指向读取数组的位置
            if read + 1 == len(chars) or chars[read+1] != ch:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write

    def compress(self, chars: List[str]) -> int:
        pre = chars[0]
        count = 1
        i = 1
        while i < len(chars):
            if chars[i] == pre:
                count += 1
                chars.pop(i)
            else:
                pre = chars[i]
                if count > 1:
                    for ch in str(count):
                        chars.insert(i, ch)
                        i += 1
                count = 1
                i += 1
        if count > 1:
            for ch in str(count):
                chars.insert(i, ch)
                i += 1
        # print(chars)
        return len(chars)


if __name__ == '__main__':
    # chars = ["a","a","a","b","b","c","c","c"]
    chars = ["1","1","1","2","2","3","4","5","5","5","5","5","6","6"]
    print(Solution().compress(chars))
