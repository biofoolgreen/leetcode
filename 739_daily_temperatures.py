"""

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # O(N**2)
        # res = []
        # for i in range(len(T)-1):
        #     cn = 1
        #     flag = False
        #     for j in range(i+1, len(T)):
        #         if T[i] > T[j]:
        #             cn += 1
        #         else:
        #             flag = True
        #             break
        #     if not flag:
        #         cn = 0
        #     res.append(cn)
        # res.append(0)
        # return res

        # 单调栈 O(N)
        res = [0]*len(T)
        stack = []
        for i in range(len(T)):
            temp = T[i]
            while stack and temp > T[stack[-1]]:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)
        return res
        



if __name__ == '__main__':
    temp = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    res = s.dailyTemperatures(temp)
    print(res)