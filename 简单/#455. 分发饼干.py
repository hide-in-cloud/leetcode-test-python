"""
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index, s_index = 0, 0
        count = 0
        while g_index < len(g) and s_index < len(s):
            if s[s_index] >= g[g_index]:
                g_index += 1
                s_index += 1
                count += 1
            else:
                s_index += 1

        return count


if __name__ == '__main__':
    g = [1,2,3]
    s = [1,2,2]
    print(Solution().findContentChildren(g, s))
