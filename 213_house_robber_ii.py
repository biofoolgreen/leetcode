"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

 

示例 1：

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：

输入：nums = [0]
输出：0
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n_houses = len(nums)
        if n_houses == 0:
            return 0
        if n_houses == 1:
            return nums[0]
        
        def subrob(nums):
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
        
        money = max(subrob(nums[:n_houses-1]), subrob(nums[1:]))
        return money


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]
    print(s.rob(nums))