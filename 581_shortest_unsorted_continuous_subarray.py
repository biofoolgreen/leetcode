"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

 

示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：

输入：nums = [1,2,3,4]
输出：0

示例 3：

输入：nums = [1]
输出：0


提示：

    1 <= nums.length <= 104
    -105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # n = len(nums)
        # sorted_nums = sorted(nums)
        # left, right = 0, n-1
        # for i in range(n):
        #     if nums[i] == sorted_nums[i]:
        #         left += 1
        #     else:
        #         break
        # # 如果全都一致，left指针指向最后一个位置，则返回0
        # if left == n:
        #     return 0
        
        # for i in range(n-1,-1,-1):
        #     if nums[i] == sorted_nums[i]:
        #         right -= 1
        #     else:
        #         break
        
        # return right-left+1
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        
        return 0 if right == -1 else right - left + 1


if __name__ == "__main__":
    sl = Solution()
    nums = [2,6,4,8,10,9,15]
    print(sl.findUnsortedSubarray(nums))