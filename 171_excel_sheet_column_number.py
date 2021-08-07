"""
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。

 

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

 

示例 1:

输入: columnTitle = "A"
输出: 1

示例 2:

输入: columnTitle = "AB"
输出: 28

示例 3:

输入: columnTitle = "ZY"
输出: 701

示例 4:

输入: columnTitle = "FXSHRXW"
输出: 2147483647

 

提示：

    1 <= columnTitle.length <= 7
    columnTitle 仅由大写英文组成
    columnTitle 在范围 ["A", "FXSHRXW"] 内

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mapper = {c:i+1 for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        n = len(columnTitle)
        res = 0
        for i, c in enumerate(columnTitle):
            res += 26**(n-i-1) * mapper[c]
        return res

if __name__ == "__main__":
    sl = Solution()
    columnTitle = "FXSHRXW"
    print(sl.titleToNumber(columnTitle))