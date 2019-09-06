'''
@Description: Easy
@Version: 
@Author: liguoying
@Date: 2019-09-06 15:20:12
'''
from typing import List

### 题目描述
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]


说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
"""
备注：
与27题 Remove Element类似，将0换成任意数字即可
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Method1 
        # for i in range(nums.count(0)):
        #     nums.remove(0)
        #     nums.append(0)
        
        # Method2
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] , nums[i]= nums[i] , nums[j]
                j += 1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    # nums = [0,0,0,0,0,1]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)