'''
@Description: Easy
@Version: 
@Author: liguoying@iiotos.com
@Date: 2019-10-12 00:18:16
@LastEditTime: 2019-10-12 00:48:35
@LastEditors: 
'''
from typing import List

### 题目描述
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
------
输入: 123
输出: 321

示例 2:
------
输入: -123
输出: -321

示例 3:
-------
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0
"""

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1].rstrip('-')
        if int(s) <= 2**31-1:
            if x >= 0:
                return int(s)
            else:
                return -int(s)
        return 0


if __name__ == '__main__':
    s = Solution()
    x = 2**10-1
    print(s.reverse(x))

