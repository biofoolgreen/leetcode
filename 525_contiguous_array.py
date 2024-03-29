"""
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。


示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0:-1}
        cnt = 0
        ans = 0
        for i, num in enumerate(nums):
            if num:
                cnt += 1
            else:
                cnt -= 1
            if cnt in hashmap:
                ans = max(ans, i - hashmap[cnt])
            else:
                hashmap[cnt] = i
        return ans
        


if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,0,0,1,1,0,1,0,1,1]
    print(s.findMaxLength(nums))