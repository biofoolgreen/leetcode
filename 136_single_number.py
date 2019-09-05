'''
@Description: Easy
@Version: 
@Author: liguoying
@Date: 2019-09-05 16:49:49
'''

from typing import List

### 题目描述
"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
----
输入: [2,2,1]
输出: 1

示例 2:
----
输入: [4,1,2,1,2]
输出: 4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Method 1
        # dics = {}
        # for i in nums:
        #     if i not in dics.keys():
        #         dics[i] = 1
        #     else:
        #         dics[i] += 1
        
        # rev_dict = {v: k for k,v in dics.items()}
        # return rev_dict[1]

        # Method 2
        # unique_list = list(set(nums))
        # sum1 = sum(unique_list) * 2
        # sum2 = sum(nums)
        # return sum1 - sum2

        # Method 3
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == "__main__":
    nums = [4,1,2,1,2]
    # nums = [2,2,1]
    s = Solution()
    print(s.singleNumber(nums))