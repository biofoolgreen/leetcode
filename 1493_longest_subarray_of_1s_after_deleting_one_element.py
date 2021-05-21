"""
给你一个二进制数组 nums ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

 

提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
示例 4：

输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4
示例 5：

输入：nums = [0,0,0]
输出：0
 

提示：

1 <= nums.length <= 10^5
nums[i] 要么是 0 要么是 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # if 0 not in nums:
        #     return len(nums)-1
        
        # ones_list = "".join(map(str, nums)).split("0")
        # res = 0
        # for i in range(len(ones_list)-1):
        #     res = max(res, len(ones_list[i])+len(ones_list[i+1]))

        # return res

        # p0(i)为「以第 i 位结尾的最长连续全 1 子数组」
        # p1(i)为「以第 i 位结尾，并且可以在某个位置删除一个 0 的最长连续全 1 子数组」
        # p0(i) = 0 if nums[i]=0 else p0(i-1)+1
        # p1(i) = p0(i-1) if nums[i]=0 else p1(i-1)+1
        ans = 0
        p0 = p1 = 0
        for num in nums:
            if num == 0:
                p1 = p0
                p0 = 0
            else:
                p0 += 1
                p1 += 1
            ans = max(p1, ans)
        if ans == len(nums):
            ans -= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,0,0,1,1,1,0,1]
    # nums = [1,1,0,1]
    # nums = [1,1,1]
    # nums = [0,1,1,1,0,1,1,0,1]
    print(s.longestSubarray(nums))