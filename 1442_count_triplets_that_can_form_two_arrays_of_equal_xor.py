"""
给你一个整数数组 arr 。

现需要从数组中取三个下标 i、j 和 k ，其中 (0 <= i < j <= k < arr.length) 。

a 和 b 定义如下：

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
注意：^ 表示 按位异或 操作。

请返回能够令 a == b 成立的三元组 (i, j , k) 的数目。

 

示例 1：

输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
示例 2：

输入：arr = [1,1,1,1,1]
输出：10
示例 3：

输入：arr = [2,3]
输出：0
示例 4：

输入：arr = [1,3,5,7,9]
输出：3
示例 5：

输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8
 

提示：

1 <= arr.length <= 300
1 <= arr[i] <= 10^8


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        lens = len(arr)
        if lens < 2:
            return 0
        
        # total = 0
        # for i in range(lens-1):
        #     for j in range(i+1, lens):
        #         val = 0
        #         for n in arr[i:j+1]:
        #             val ^= n
        #         if val == 0:
        #             total += j-i
        # return total
        xor_arr = [0]
        for num in arr:
            xor_arr.append(xor_arr[-1]^num)

        total = 0
        for i in range(lens):
            for j in range(i+1, lens):
                tmp = xor_arr[i]^xor_arr[j+1]
                if tmp==0:
                    total += j-i
        return total


if __name__ == "__main__":
    s = Solution()
    arr = [2,2]
    # arr = [2,3,1,6,7]
    # arr = [1,1,1,1,1]
    print(s.countTriplets(arr))

