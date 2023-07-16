"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """纵向扫描"""
        min_str = min(strs)  # 最短字符串长度
        for k in range(len(min_str)):  # 只需检索最短字符串长度的范围,k指向字符串的字符
            for string in strs:  # string指向字符串数组的字符串
                if string[k] != min_str[k]:
                    return min_str[:k]  # 取k之前的子字符串
        return min_str

    def longestCommonPrefix2(self, strs) -> str:
        """横向扫描"""
        prefix = min(strs)
        for string in strs:
            length = len(prefix)
            for k in range(length):
                if string[k] != prefix[k]:
                    prefix = string[:k]  # 对于每个遍历到的字符串，更新最长公共前缀
                    break
            if not prefix:  # 公共前缀为空
                break
        return prefix

    def longestCommonPrefix3(self, strs) -> str:
        """利用zip函数"""
        prefix = ''
        chars = map(set, zip(*strs))  # zip返回一个对象,map映射把每组字符去重.
        for k, char in enumerate(chars):
            list_char = list(char)
            if len(list_char) == 1:  # 去重后只剩下一个字符,说明该字符是公共前缀
                prefix += list_char[0]
            else:
                break
        return prefix

    def longestCommonPrefix4(self, strs) -> str:
        """利用min()和max()的特性,字符串比较是按照ascii值排列的,所以只需要比较最大最小的公共前缀就是整个数组的公共前缀"""
        min_str, max_str = min(strs), max(strs)
        for k in range(len(min_str)):
            if min_str[k] != max_str[k]:
                return min_str[:k]
        return min_str


if __name__ == '__main__':
    # strs = ["carry","care","carhdhd"]
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix4(strs))
