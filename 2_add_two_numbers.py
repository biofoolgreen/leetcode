'''
@Description: Medium
@Version: 
@Author: liguoying
@Date: 2019-09-05 16:06:22
'''
from typing import List

### 题目描述
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例
-----
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1.val:
            return l2
        if not l2.val:
            return l1
        
        init = l1.val + l2.val
        carry = init // 10
        reminder = init % 10
        head = ListNode(reminder)
        cur = head
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            tmp = l1.val + l2.val + carry
            carry = tmp // 10
            reminder = tmp % 10
            cur.next = ListNode(reminder)
            cur = cur.next
        
        if carry>0:
            cur.next = ListNode(carry)
            cur = cur.next
        return head             

def addTwoNumbers(l1: List, l2: List) -> List:
    len1 = len(l1)
    len2 = len(l2)
    if len1 == 0:
        return l2
    if len2 == 0:
        return l1
    
    total = []
    carry = 0
    maxlen = max(len1, len2)
    for i in range(maxlen):
        if i > len1-1:
            tmp = l2[i] + carry
        elif i > len2-1:
            tmp = l1[i] + carry
        else:
            tmp = l1[i] + l2[i] + carry
        carry = tmp // 10
        reminder = tmp % 10
        total.append(reminder)
    if carry:
        total.append(carry)
    return total



if __name__ == "__main__":
    # l1_nums = [2,4,3]
    # l2_nums = [5,6,4]
    l1_nums = [9,9,9,9,9,9,9]
    l2_nums = [9,9,9,9]
    # l1 = ListNode(None)
    # l2 = ListNode(None)
    # for i in l1_nums:
    #     l1.next = i
    #     l1.val = l1.next
    # for i in l2_nums:
    #     l2.next = i
    #     l2.val = l2.next
    # print(f"l1={l1}, l2={l2}")
    print(addTwoNumbers(l1_nums, l2_nums))
