"""
有台奇怪的打印机有以下两个特殊要求：

打印机每次只能打印由 同一个字符 组成的序列。
每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。

 
示例 1：

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。
示例 2：

输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
 

提示：

1 <= s.length <= 100
s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strange-printer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def strangePrinter(self, s: str) -> int:
        # dp[i][j]：表示字符串 s 在区间 [i, j]中需要最少的打印次数。
        # dp[i][j] = dp[i][j-1] if s[j]==s[j-1]
        # dp[i][j] = min(dp[i][k]+dp[k+1][j]) if s[j]!=s[j-1]

        n = len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = 10000 # 任意大值
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
        return dp[0][n-1]

        

if __name__ == "__main__":
    sl = Solution()
    s = "aaabbb"
    print(sl.strangePrinter(s))