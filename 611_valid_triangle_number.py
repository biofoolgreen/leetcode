"""
给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。

示例 1:

输入: [2,2,3,4]
输出: 3
解释:
有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

注意:

    数组长度不超过1000。
    数组里整数的范围为 [0, 1000]。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-triangle-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from functools import reduce
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # # 排序+二分
        # n = len(nums)
        # sorted_nums = sorted(nums)
        # cnt = 0
        # for i in range(n-2):
        #     for j in range(i+1, n-1):
        #         left, right, k = j+1, n-1, j
        #         while left<=right:
        #             mid = (left+right) // 2
        #             if sorted_nums[mid] < sorted_nums[i]+sorted_nums[j]:
        #                 k = mid
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1
        #         cnt += k-j
        # return cnt

        # 排序+双指针
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                while k + 1 < n and nums[k + 1] < nums[i] + nums[j]:
                    k += 1
                ans += max(k - j, 0)
        return ans

if __name__ == "__main__":
    sl = Solution()
    nums = [7,0,0,0]
    print(sl.triangleNumber(nums))