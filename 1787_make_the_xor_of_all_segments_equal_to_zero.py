"""
给你一个整数数组 nums​​​ 和一个整数 k​​​​​ 。区间 [left, right]（left <= right）的 异或结果 是对下标位于 left 和 right（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：nums[left] XOR nums[left+1] XOR ... XOR nums[right] 。

返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。

 

示例 1：

输入：nums = [1,2,0,3,0], k = 1
输出：3
解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]
示例 2：

输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
输出：3
解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]
示例 3：

输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
输出：3
解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3]
 

提示：

1 <= k <= nums.length <= 2000
​​​​​​0 <= nums[i] < 210

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # x 的范围为 [0, 2^10)
        MAXX = 2**10
        
        n = len(nums)
        f = [float("inf")] * MAXX
        # 边界条件 f(-1,0)=0
        f[0] = 0
        
        for i in range(k):
            # 第 i 个组的哈希映射
            count = Counter()
            size = 0
            for j in range(i, n, k):
                count[nums[j]] += 1
                size += 1

            # 求出 t2
            t2min = min(f)

            g = [t2min] * MAXX
            for mask in range(MAXX):
                # t1 则需要枚举 x 才能求出
                for x, countx in count.items():
                    g[mask] = min(g[mask], f[mask ^ x] - countx)
            
            # 别忘了加上 size
            f = [val + size for val in g]

        return f[0]


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,0,3,0]
    k = 1
    nums = [3,4,5,2,1,7,3,4,7]
    k = 3
    nums = [1,2,4,1,2,5,1,2,6]
    k = 3
    print(s.minChanges(nums, k))