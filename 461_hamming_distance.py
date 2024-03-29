"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # strx = "{:0>32b}".format(x)
        # stry = "{:0>32b}".format(y)
        # return sum(i!=j for i,j in zip(strx, stry))

        return sum(i=="1" for i in "{:b}".format(x|y))


if __name__ == "__main__":
    s = Solution()
    x, y = 1, 4
    print(s.hammingDistance(x, y))