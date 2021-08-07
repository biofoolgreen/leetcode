"""
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
示例 1：
输入：points = [[1,1],[2,2],[3,3]]
输出：3

示例 1：
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4

提示：

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        if num_points <= 2:
            return num_points
        kmap = {}
        for i in range(num_points-1):
            x0, y0 = points[i]
            for j in range(i+1, num_points):
                x1, y1 = points[j]
                if x1 == x0:
                    k = "k"
                    b = x1
                else:
                    k = (y1-y0)/(x1-x0)
                    b = y1 - k*x1
                if (k,b) not in kmap:
                    kmap[(k,b)] = [points[i]]
                if points[j] not in kmap[(k,b)]:
                    kmap[(k,b)].append(points[j])

        max_points = len(max(kmap.values(), key=len))
        return max_points

if __name__ == "__main__":
    sl = Solution()
    # points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    # points = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
    points = [[-6,-1],[3,1],[12,3]]
    print(sl.maxPoints(points))