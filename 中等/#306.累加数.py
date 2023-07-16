"""
累加数是一个字符串，组成它的数字可以形成累加序列。
一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。

说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:  # 累加序列至少包含 3 个数
            return False

        for i in range(1, n//2+1):  # 第一个数的长度最大为n//2
            if i > 1 and num[0] == '0':  # 不存在前导零的数
                break

            max_len_group = (n-i) // 2  # 分组的最大长度为除去第一个数的长度再除以2(当3个数时)
            for len_group in range(1, max_len_group+1):  # 按每组的不同长度遍历字符串
                index = i + len_group
                if len_group > 1 and num[i] == '0':  # 不存在前导零的数
                    break
                fib = [int(num[:i]), int(num[i:index])]  # 先确定前两个数
                print(fib)

                # 添加fib累加数组
                while index < n:
                    next_fib = fib[-2] + fib[-1]  # 预测下一个数
                    len_next_group = len(str(next_fib))  # 下一个数的长度
                    if next_fib == int(num[index:index+len_next_group]):  # 按照长度找下一个数
                        fib.append(next_fib)
                        print(fib)
                        index = index + len_next_group
                    else:
                        break
                if index == n:
                    return True
        return False


if __name__ == '__main__':
    # num = "112358"
    # num = "199100199"
    # num = "123"
    # num = "1023"
    # num = "211738"
    # num = "0235813"
    # num = "198019823962"
    num = "199111992"
    print(Solution().isAdditiveNumber(num))
