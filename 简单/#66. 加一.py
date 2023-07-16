"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """转为字符串再转整型操作"""
        s = "".join(map(str, digits))  # 转字符串
        s = list(str(int(s) + 1))  # 转整型进行加一操作后再转回字符串
        return list(map(int, s))  # 转回整型数组

    def plusOne2(self, digits: List[int]) -> List[int]:
        """在原数组上操作"""
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits
        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    # digits = [9,9,9]
    digits = [8,8,8]
    print(Solution().plusOne2(digits))
