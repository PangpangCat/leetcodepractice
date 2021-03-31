# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseLinkedList(self,li: ListNode) -> ListNode:
        pre = None
        cur = li
        next = None
        while cur!= None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseLinkedList(l1)
        l2 = self.reverseLinkedList(l2)
        #创建一个新的Linked list
        dummy = tail = ListNode(0) #dummy和tail两个指针都指向一个全新的的node - ListNode(0)
        s = 0
        carry = 0 #carry是进位 可以为1 或者0
        while l1 or l2 or carry: #l1 l2 carry任意不为空的情况下循环
            s = (l1.val if l1 else 0) +(l2.val if l2 else 0) + carry
            tail.next = ListNode(s % 10)
            tail = tail.next
            carry = 1 if s >= 10 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # return dummy.next

        dummy.next = self.reverseLinkedList(dummy.next)
        return dummy.next

# Time Complexity: O(max(n,m))
# Space Complexity: O(max(n,m))











