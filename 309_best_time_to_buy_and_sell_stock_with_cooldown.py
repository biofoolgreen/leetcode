"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # f[i]: 第i天结束之后的「累计最大收益」
        # 第i天结束后的3种状态
        # 1. 持有股票：f[i][0] ==> 前一天持有（f[i-1][0]），前一天没有持有且不处于冷冻期，今天买的（f[i-1][2]-prices[i]）
        # 2. 未持有股票且处于冷冻期： f[i][1] ===> 前一天卖出（f[i-1][0] + prices[i]）
        # 3. 未持有股票且不处于冷冻期：f[i][2] ===> 前一天未持有，前一天冷冻期今天没买（f[i-1][1]），前一天不是冷冻期今天也没买（f[i-1][2]）
        # 第一种情况：f[i][0] = max(f[i-1][0], f[i-1][2]-prices[i])
        # 第二种情况：f[i][1] = f[i-1][0] + prices[i]
        # 第三种情况：f[i][2] = max(f[i-1][2], f[i-1][1])
        if not prices:
            return 0
        
        days = len(prices)
        dp = [[0,0,0] for _ in range(days)]
        dp[0][0] = -prices[0]

        for i in range(1, days):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max([dp[days-1][0], dp[days-1][1], dp[days-1][2]])


if __name__ == '__main__':
    s = Solution()
    # prices = [1,2,3,0,2]
    prices = [6,1,3,2,4,7]
    print(s.maxProfit(prices))