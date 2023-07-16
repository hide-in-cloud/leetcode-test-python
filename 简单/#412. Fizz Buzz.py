"""
写一个程序，输出从 1 到 n 数字的字符串表示。
1. 如果 n 是3的倍数，输出“Fizz”；
2. 如果 n 是5的倍数，输出“Buzz”；
3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ans.append('FizzBuzz')
            elif i % 5 == 0:
                ans.append('Buzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            else:
                ans.append(str(i))
        return ans

    def fizzBuzz2(self, n: int) -> List[str]:
        """散列表 + 字符串连接"""
        ans = []
        dic = {3:'Fizz', 5:'Buzz'}
        for i in range(1, n+1):
            num_str = ""
            for key in dic.keys():
                if i % key == 0:
                    num_str += dic[key]
            if not num_str:
                num_str += str(i)
            ans.append(num_str)
        return ans


if __name__ == '__main__':
    n = 15
    print(Solution().fizzBuzz2(n))
