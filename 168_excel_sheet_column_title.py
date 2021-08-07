"""
给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

示例 1：

输入：columnNumber = 1
输出："A"
示例 2：

输入：columnNumber = 28
输出："AB"
示例 3：

输入：columnNumber = 701
输出："ZY"
示例 4：

输入：columnNumber = 2147483647
输出："FXSHRXW"
 

提示：

1 <= columnNumber <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapper = {i+1:c for i, c in enumerate("abcdefghijklmnopqrstuvwxyz".upper())}
        res = ""

        while columnNumber:
            reminder = columnNumber % 26
            if reminder == 0: reminder = 26
            res = mapper[reminder] + res
            columnNumber = (columnNumber-reminder) // 26
        return res



if __name__ == "__main__":
    sl = Solution()
    columnNumber = 701
    print(sl.convertToTitle(columnNumber))