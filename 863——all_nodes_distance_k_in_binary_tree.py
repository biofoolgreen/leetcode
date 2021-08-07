"""
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

 

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。

 

提示：

    给定的树是非空的。
    树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
    目标结点 target 是树上的结点。
    0 <= K <= 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
from collections import defaultdict, deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(root, parent):
            if root is None:
                return None
            if parent:
                graph[parent.val].append(root.val)
                graph[root.val].append(parent.val)
            build_graph(root.left, root)
            build_graph(root.right, root)
        
        build_graph(root, None)

        ans = []
        visited = set([target.val])
        queue = deque([target.val])
        # BFS 遍历
        while queue:
            qlen = len(queue)
            for i in range(qlen):
                cur = queue.popleft()
                if k == 0:
                    ans.append(cur)
                else:
                    for n in graph[cur]:
                        if n not in visited:
                            visited.add(n)
                            queue.append(n)
            k -= 1
        return ans


if __name__ == "__main__":
    sl = Solution()
    root = [3,5,1,6,2,0,8,None,None,7,4]
    target = 5
    k = 2
    print(sl.distanceK(root, target, k))