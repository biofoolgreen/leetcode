"""
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

 

示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1
 

提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 记数组的元素和为sum，添加 - 号的元素之和为 neg，则其余添加 + 的元素之和为 sum−neg，得到的表达式的结果为
        # (sum−neg)−neg=sum−2⋅neg=target
        # ==> neg = (sum - target)/2
        # 问题转化成在数组 nums 中选取若干元素，使得这些元素之和等于neg，计算选取元素的方案数。
        # dp[i][j]: 从数组0到i的和为j的方案数
        # dp[i][j] = dp[i-1][j]+ dp[i-1][j-nums[i]] if j>=nums[i]
        # dp[i][j] = dp[i-1][j] if j<nums[i]
        # dp[0][j] = 1 if j=0 else 0
        n = len(nums)
        sums = sum(nums)
        diff = sums - target
        if diff < 0 or diff % 2 != 0:
            return 0
        neg = int(diff / 2)
        # dp = [[0]*(neg+1) for _ in range(n+1)]
        # print(len(dp),len(dp[0]))
        # dp[0][0] = 1
        # for j in range(1, neg+1):
        #     dp[0][j] = 0
        
        # for i in range(1, n+1):
        #     num = nums[i-1]
        #     for j in range(neg+1):
        #         dp[i][j] = dp[i-1][j]
        #         if j>=num:
        #             dp[i][j] += dp[i-1][j-num]
        # print(dp)
        # return dp[n][neg]
        dp = [0 for _ in range(neg+1)]
        dp[0] = 1
        for num in nums:
            print(neg, num)
            if neg >= num:
                for j in range(neg, num-1, -1):
                    dp[j] += dp[j-num]
                    print(dp)
        return dp[neg]


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1]
    target = 3
    print(s.findTargetSumWays(nums, target))