"""
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。

子数组 是数组的一段连续部分。

 

示例 1：

输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]

示例 2：

输入：nums = [0,0,0,0,0], goal = 0
输出：15

 

提示：

    1 <= nums.length <= 3 * 104
    nums[i] 不是 0 就是 1
    0 <= goal <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-subarrays-with-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        mapper = defaultdict(int)
        # mapper[1] = sum(nums)
        # mapper[0] = n - sum(nums)
        
        # winsize = 2
        # while winsize <= n:
        #     for i in range(n-winsize+1):
        #         subn = nums[i:i+winsize]
        #         s = sum(nums[i:i+winsize])
        #         mapper[s] = mapper.get(s, 0) + 1
        #     winsize += 1
        # return mapper.get(goal,0)
        res = 0
        presum = 0
        for num in nums:
            mapper[presum] += 1
            presum += num
            res += mapper[presum-goal]
        return res

if __name__ == "__main__":
    sl = Solution()
    # nums = [1,0,1,0,1]
    # goal = 2
    nums = [0,0,0,0,0]
    goal = 0
    print(sl.numSubarraysWithSum(nums, goal))
