"""
在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。
移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
"""
import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # counts = collections.Counter(moves)
        # if counts['L'] == counts['R'] and counts['U'] == counts['D']:
        #     return True
        # else:
        #     return False

        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')


if __name__ == '__main__':
    # moves = "UD"
    moves = "LRRL"
    print(Solution().judgeCircle(moves))
