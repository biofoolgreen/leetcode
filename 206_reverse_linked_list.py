'''
@Description: 
@Version: 
@Author: liguoying@iiotos.com
@Date: 2019-11-25 23:31:24
@LastEditTime: 2019-11-26 00:12:38
@LastEditors: 
'''

### 题目描述
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        我们可以申请两个指针，第一个指针叫pre，最初是指向null的。
        第二个指针cur指向head，然后不断遍历cur。
        每次迭代到cur，都将cur的next指向pre，然后pre和cur前进一位。
        都迭代完了(cur变成null了)，pre就是最后一个节点了。
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
        # 递归方式
        # 1.当头结点为空或下一个结点为空的时候返回该结点
        if not head or not head.next:
            return head
        # 获取下一个结点
        next_node = head.next
        # 递归反转
        res = self.reverseList(next_node)
        # 头结点接到反转链表的尾部
        next_node.next = head
        head.next = None
        return res