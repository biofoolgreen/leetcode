"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

0 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if not houses:
            return 0
        # 子问题：
        # f(k) = 偷 [0..k) 房间中的最大金额

        # f(0) = 0
        # f(1) = nums[0]
        # f(k) = max{ rob(k-1), nums[k-1] + rob(k-2) }
        max_robbed_money = [0]*(houses+1)
        max_robbed_money[0] = 0
        max_robbed_money[1] = nums[0]
        for i in range(2, houses+1):
            max_robbed_money[i] = max(max_robbed_money[i-1], max_robbed_money[i-2]+nums[i-1])
        return max_robbed_money[houses]


if __name__ == "__main__":
    s = Solution()
    nums = [2,7,9,3,1]
    print(s.rob(nums))