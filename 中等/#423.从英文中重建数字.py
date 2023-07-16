"""
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。
(zero,one,two,three,four,five,six,seven,eight,nine)
"""
import collections


def originalDigits1(s: str) -> str:
    """利用单词的特征字母来逐步判断"""
    ans = ""
    s = list(s)
    # mp = {}
    # symbols = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    first = ['z', 'w', 'u', 'x', 'g']
    first_word = ['zero', 'two', 'four', 'six', 'eight']
    first_number = ['0', '2', '4', '6', '8']
    second = ['s', 'h', 'f']
    second_word = ['seven', 'three', 'five']
    second_number = ['7', '3', '5']
    third = ['o', 'i']
    third_word = ['one', 'nine']
    third_number = ['1', '9']

    c1 = collections.Counter(s)  # 统计
    for i, symbol in enumerate(first):
        if c1[symbol]:
            num = c1[symbol]  # 特征单词对应频次
            ans += first_number[i] * num  # 记录结果
            for char in first_word[i]:
                c1[char] -= num  # 从字典中删除该单词
    # print(s)
    for i, symbol in enumerate(second):
        if c1[symbol] and c1[symbol] > 0:
            num = c1.get(symbol)
            ans += second_number[i] * num
            for char in second_word[i]:
                c1[char] -= num
    # print(s)
    # print(c1)
    for i, symbol in enumerate(third):
        if c1[symbol] and c1[symbol] > 0:
            num = c1[symbol]
            ans += third_number[i] * num
            for char in third_word[i]:
                c1[char] -= num
    # print(c1)
    # print(mp)
    return "".join(sorted(ans))


def originalDigits(s: str) -> str:
    """利用单词的特征字母来逐步判断"""
    symbols = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ans = ""
    n0 = s.count('z')
    n2 = s.count('w')
    n4 = s.count('u')
    n6 = s.count('x')
    n8 = s.count('g')
    n7 = s.count('s') - n6
    n3 = s.count('h') - n8
    n5 = s.count('f') - n4
    n1 = s.count('o') - n0 - n2 - n4
    n9 = s.count('i') - n5 - n6 - n8
    nums = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
    for i, n in enumerate(nums):
        ans += str(i)*n
    return ans


if __name__ == '__main__':
    s = "owoztneoer"
    # s = "fviefuro"
    print(originalDigits(s))
