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
        ###
        # wrong answer
        ###
        list1 = []
        list2 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        
        len1 = len(list1)
        len2 = len(list2)
        num1 = int("".join(list1[::-1]))
        num2 = int("".join(list2[::-1]))
        add_num = num1 + num2
        num_str = str(add_num)
        rev_num_str = num_str[::-1]
        return [int(n) for n in rev_num_str.split()]


if __name__ == "__main__":
    l1 = []