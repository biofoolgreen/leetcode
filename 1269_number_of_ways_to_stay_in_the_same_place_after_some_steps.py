"""
有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。

 

示例 1：

输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动
示例  2：

输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动
示例 3：

输入：steps = 4, arrLen = 2
输出：8
 

提示：

1 <= steps <= 500
1 <= arrLen <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # dp[step, pos]: 走step步回到pos的方案数
        # dp[step, pos] = dp[step-1][pos] + dp[step-1][pos-1] + dp[step-1][pos+1]
        # 下标pos最远的地方
        max_columns = min(arrLen-1, steps)
        dp = [[0]*(max_columns+1)  for _ in range(steps+1)]
        mod = 10**9+7
        # 初始条件
        dp[0][0] = 1
        # 转移方程
        for step in range(1, steps+1):
            for pos in range(max_columns+1):
                if pos == 0:
                    dp[step][pos] = (dp[step-1][pos] + dp[step-1][pos+1]) % mod
                elif pos == max_columns:
                    dp[step][pos] = (dp[step-1][pos] + dp[step-1][pos-1]) % mod
                else:
                    dp[step][pos] = (dp[step-1][pos] + dp[step-1][pos-1] + dp[step-1][pos+1]) % mod
        return dp[steps][0]


if __name__ == "__main__":
    s = Solution()
    steps, arrLen = 4, 2
    print(s.numWays(steps, arrLen))