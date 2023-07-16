"""
给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
"""
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """只计算战舰的右下角"""
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    if (c == 0 or board[r][c-1] == ".") and (r == 0 or board[r-1][c] == "."):
                        count += 1
        return count

    def countBattleships2(self, board: List[List[str]]) -> int:
        """修改多余的X"""
        numRows = len(board)
        numColumns = len(board[0])
        count = 0
        for r in range(numRows):
            for c in range(numColumns):
                if board[r][c] == "X":
                    count += 1
                    i, j = r, c
                    while j+1 < numColumns and board[i][j+1] == "X":
                        board[i][j+1] = "."
                        j += 1
                    while i+1 < numRows and board[i+1][c] == "X":
                        board[i+1][j] = "."
                        i += 1
        # print(board)
        return count


if __name__ == '__main__':
    board = [["X","X",".","X"],[".",".",".","X"],["X","X",".","X"]]
    print(Solution().countBattleships(board))
