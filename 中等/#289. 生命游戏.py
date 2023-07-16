"""
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），
或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

        m, n = len(board), len(board[0])
        copy_board = [[board[row][col] for col in range(n)] for row in range(m)]

        for r in range(m):
            for c in range(n):
                count = 0
                for neighbor in neighbors:
                    i = r + neighbor[0]
                    j = c + neighbor[1]
                    if (0 <= i < m) and (0 <= j < n) and copy_board[i][j] == 1:
                        count += 1
                if copy_board[r][c] == 1 and (count < 2 or count > 3):
                    board[r][c] = 0
                elif copy_board[r][c] == 0 and count == 3:
                    board[r][c] = 1
        for r in range(m):
            print(board[r])

    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """ -1 代表这个细胞过去是活的现在死了, 2 代表这个细胞过去是死的现在活了"""
        neighbors = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                count = 0
                for neighbor in neighbors:
                    i = r + neighbor[0]
                    j = c + neighbor[1]
                    if (0 <= i < m) and (0 <= j < n) and abs(board[i][j]) == 1:
                        count += 1
                if board[r][c] == 1 and (count < 2 or count > 3):
                    board[r][c] = -1  # -1 代表这个细胞过去是活的现在死了
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2  # 2 代表这个细胞过去是死的现在活了
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0
        for r in range(m):
            print(board[r])

    def gameOfLife3(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """ 活细胞去影响周围的8个格子,用十位数记录周围的活细胞数,个位数记录当前状态 """
        neighbors = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

        m, n = len(board), len(board[0])

        def affect(r, c):
            """活细胞去影响周围的8个格子"""
            for neighbor in neighbors:
                i = r + neighbor[0]
                j = c + neighbor[1]
                if 0 <= i < m and 0 <= j < n:
                    board[i][j] += 10
        # 记录状态
        for r in range(m):
            for c in range(n):
                if board[r][c] % 10 == 1:  # 个位为1表示活
                    affect(r,c)
        # 下一状态
        for r in range(m):
            for c in range(n):
                value = board[r][c]
                if value // 10 == 3:
                    board[r][c] = 1
                elif value % 10 == 1 and value // 10 == 2:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
        for r in range(m):
            print(board[r])


if __name__ == '__main__':
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print(Solution().gameOfLife3(board))
