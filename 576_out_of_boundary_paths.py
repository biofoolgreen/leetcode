"""
给定一个 m × n 的网格和一个球。球的起始坐标为 (i,j) ，你可以将球移到相邻的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你最多可以移动 N 次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 109 + 7 的值。

示例 1：

输入: m = 2, n = 2, N = 2, i = 0, j = 0
输出: 6

示例 2：

输入: m = 1, n = 3, N = 3, i = 0, j = 1
输出: 12

说明:

球一旦出界，就不能再被移动回网格内。
网格的长度和高度在 [1,50] 的范围内。
N 在 [0,50] 的范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/out-of-boundary-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # f(i,j,N): 球在（i，j), 移动N次可以把球移除边界的次数
        # 从1开始到N每次刷新m*n的矩阵dp，记录第k次矩阵里每个点能飞出边界的路径数
        # 第k次的dp[i][j]所代表的路径和等于上下左右的节点第k-1次路径的累加和
        # 如果ij代表的是边界的点，那么可能它往上下左右移动会出现直接出界的情况，此时直接+1。
        # 每次只需要维护两个m*n的矩阵，一个是第k次的，一个是第k-1次的

        prev = [[0]*n for _ in range(m)]
        direction = [
            [-1,0], [1,0], [0,-1], [0,1]
        ]
        # mat[0][0] = mat[m-1][n-1] = mat[m-1][0] = mat[0][n-1] = 2
        for step in range(N):
            cur = [[0]*n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx,dy in direction:
                        move_x = x+dx
                        move_y = y+dy
                        # 如果移动过后已经出了边界这时直接+1，
                        # xy移动前就在边界上，这1次出界的移动带来了1条新路径
                        if move_x == -1 or move_x == m or move_y == -1 or move_y == n:
                            cur[x][y] += 1
                         # 每次增加的路径一定只跟上一次的点有关，跟本次的上下左右没有任何关系
                        else:
                            cur[x][y] += prev[move_x][move_y]
            prev = cur
        return cur[i][j] % 1000000007

if __name__=="__main__":
    s = Solution()
    print(s.findPaths(2,2,2,0,0))
