'''
@Description: 
@Version: 
@Author: liguoying
@Date: 2019-09-04 14:30:35
'''

from typing import List

### 题目描述
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

"""

class Solution:
    # # 暴力法O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     lens = len(nums)
    #     for i in range(lens-1):
    #         for j in range(i+1, lens):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return []

    # 字典O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in dic.keys():
                return [dic[res], i]
            dic[num] = i
        return []

if __name__ == "__main__":
    s = Solution()
    nums1 = [3, 2, 4]
    target1 = 6
    print(s.twoSum(nums1, target1))

    nums2 = [-3,4,3,90]
    target2 = 0
    print(s.twoSum(nums2, target2))

