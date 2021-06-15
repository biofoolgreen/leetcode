"""
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

 

示例 1：

输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
示例 2：

输入：stones = [31,26,33,21,40]
输出：5
示例 3：

输入：stones = [1,2]
输出：1
 

提示：

1 <= stones.length <= 30
1 <= stones[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/last-stone-weight-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 记数组的元素和为sum，添加 - 号的元素之和为 neg，则其余添加 + 的元素之和为 sum−neg，得到的表达式的结果为
        # (sum−neg)−neg=sum−2⋅neg=target
        # 要使target尽可能小，就需要neg尽可能接近[sum/2], 从而本问题转化为背包容量为⌊sum/2⌋，
        # 物品重量和价值均为 stones i的 0-1 背包问题
        # dp[i+1][j]: 从数组0到i能否凑出重要j
        # dp[i+1][j] = dp[i][j] | dp[i][j-stones[i]] if j>=stones[i]
        # dp[i+1][j] = dp[i][j] if j<stones[i]
        # dp[0][j] = True if j=0 else False
        n = len(stones)
        total = sum(stones)
        neg = sum(stones) // 2
        # dp = [[False]*(neg+1) for _ in range(n+1)]

        # dp[0][0] = True
        # for j in range(1, neg+1):
        #     dp[0][j] = False
        
        # for i in range(n):
        #     for j in range(neg+1):
        #         if j < stones[i]:
        #             dp[i+1][j] = dp[i][j]
        #         else:
        #             dp[i+1][j] = dp[i][j-stones[i]] or dp[i][j]
        # ans = None
        # for j in range(neg, -1, -1):
        #     if dp[n][j]:
        #         ans = total - 2*j
        #         break
        # return ans
        dp = [False] * (neg + 1)
        dp[0] = True

        for weight in stones:
            for j in range(neg, weight - 1, -1):
                dp[j] |= dp[j - weight]
        
        ans = None
        for j in range(neg, -1, -1):
            if dp[j]:
                ans = total - 2 * j
                break
        
        return ans


if __name__ == "__main__":
    s = Solution()
    # stones = [2,7,4,1,8,1]
    stones = [31,26,33,21,40]
    print(s.lastStoneWeightII(stones))