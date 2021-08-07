"""
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

    lefti 是第 i 座建筑物左边缘的 x 坐标。
    righti 是第 i 座建筑物右边缘的 x 坐标。
    heighti 是第 i 座建筑物的高度。

天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

 

示例 1：

输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
解释：
图 A 显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。

示例 2：

输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]

 

提示：

    1 <= buildings.length <= 104
    0 <= lefti < righti <= 231 - 1
    1 <= heighti <= 231 - 1
    buildings 按 lefti 非递减排序

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-skyline-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import defaultdict
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # mapper = defaultdict(list)  # 每个x点有的所有楼房高度

        # for left, right, height in buildings:
        #     for i in range(left, right+1):
        #         mapper[i] = mapper.get(i, []) + [height]
        
        # mapper = sorted(mapper.items(), key=lambda x: x[0])
        # res = []
        # # 第一个左端点
        # prex, prey = buildings[0][0], buildings[0][2]
        # for x, y in mapper:
        #     res.append([x, max(y)])
        # return res

        n = len(buildings)
        boundaries = []
        for l, r, h in buildings:
            boundaries.append([l, h])
            boundaries.append([r, 0])
        boundaries = sorted(boundaries, key=lambda x: (x[0], -x[1]))
        return boundaries


        


if __name__ == "__main__":
    sl = Solution()
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    print(sl.getSkyline(buildings))