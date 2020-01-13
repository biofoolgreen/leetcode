'''
@Description: 
@Version: 
@Author: liguoying@iiotos.com
@Date: 2019-11-26 00:12:57
@LastEditTime: 2019-12-09 23:35:43
@LastEditors: 
'''
### 题目描述
"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        # left, right = head, head
        # stop = False
        # def recurse_and_reverse(right, m, n):
        #     nonlocal left, stop
        #     if n == 1:
        #         return None
        #     right = right.next
        #     if m > 1:
        #         left = left.next
            
        #     recurse_and_reverse(right, m-1, n-1)
        #     if left == right or right.next == left:
        #         stop = True
            
        #     if not stop:
        #         left.val, right.val = right.val, left.val
        #         left = left.next
        
        # recurse_and_reverse(right, m, n)
        # return head

        cur, pre = head, None
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        
        tail, con = cur, pre
        while n:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third
            n -= 1
        
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
            