"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

进阶：

你可以设计时间复杂度为 O(n2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens < 2:
            return nums
        # 单调栈-Wrong
        # stack = [nums[0]]
        # for i in range(1, lens):
        #     cur_num = nums[i]
        #     if cur_num <= stack[-1]:
        #         continue
        #     while stack and cur_num <= stack[-1]:
        #         last = stack.pop()
        #         print(f"last={last}")
        #     stack.append(cur_num)
        #     print(f"cur_num={cur_num}, stack={stack}")
        # return stack
        # 子问题
        # f(n): 从1.。。n的最长递增子序列
        # f(0) = 0
        # f(1) = 1
        # f(k) = 
        max_sub_seq = []
        for i in range(lens):
            max_sub_seq.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    max_sub_seq[i] = max(max_sub_seq[i], max_sub_seq[j]+1)
        print(max_sub_seq)
        return max(max_sub_seq)

if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    # nums = [0,1,0,3,2,3]
    # nums = [7,7,7,7,7,7,7]
    print(s.lengthOfLIS(nums))